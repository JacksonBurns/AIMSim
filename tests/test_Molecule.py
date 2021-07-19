""" Test the methods of the Molecule class """
from os import remove, mkdir
import os.path
from shutil import rmtree
import unittest

import numpy as np
import pandas as pd
import rdkit
from rdkit.Chem import MolFromSmiles
from rdkit.Chem.rdmolfiles import MolToPDBFile

from molSim.chemical_datastructures import Molecule, MoleculeSet
from molSim.exceptions import NotInitializedError
from molSim.ops import Descriptor, SimilarityMeasure


SUPPORTED_SIMILARITIES = ['tanimoto', 'jaccard', 'negative_l0',
                          'negative_l1', 'negative_l2']
SUPPORTED_FPRINTS = ['morgan_fingerprint', 'topological_fingerprint']


class TestMolecule(unittest.TestCase):
    """
    Tests for methods of Molecule class.

    """
    def test_molecule_created_with_no_attributes(self):
        """
        Test for creation of empty Molecule object with no attributes.

        """
        test_molecule = Molecule()
        self.assertIsNone(test_molecule.mol_graph,
                          'Expected attribute mol_graph to be None '
                          'for uninitialized Molecule')
        self.assertIsNone(test_molecule.mol_text,
                          'Expected attribute mol_text to be None '
                          'for uninitialized Molecule')
        self.assertIsNone(test_molecule.mol_property_val,
                          'Expected attribute mol_property_val to be None '
                          'for uninitialized Molecule')
        self.assertFalse(test_molecule.descriptor.check_init(),
                         'Expected molecule.descriptor to be unitialized  '
                         'for uninitialized Molecule')

    def test_molecule_created_w_attributes(self):
        """
        Test to create Molecule object with descriptor value (list) and a 
        response scalar.

        """
        test_molecule = Molecule(mol_text='test_molecule',
                                 mol_property_val=42,
                                 mol_descriptor_val=[1, 2, 3])
        self.assertEqual(test_molecule.mol_text, 'test_molecule',
                         'Expected mol_text attribute to be set.')
        self.assertEqual(test_molecule.mol_property_val, 42,
                         'Expected mol_property_val to be set.')
        self.assertIsInstance(test_molecule.descriptor.to_numpy(), np.ndarray,
                              'Expected descriptor.to_numpy()to be np.ndarray')
        self.assertTrue(np.all(
            test_molecule.descriptor.to_numpy() == np.array([1, 2, 3])),
                         "Expected descriptor.to_numpy() to be array[1, 2, 3]")
        self.assertEqual(test_molecule.descriptor.label_, 'arbitrary',
                         'Expected descriptor.label to be arbitrary since '
                         'it was initialized by list/array')

    def test_set_molecule_from_smiles(self):
        """
        Test to create Molecule object by reading SMILES string.

        """
        test_smiles = 'CC'
        test_molecule = Molecule()
        test_molecule._set_molecule_from_smiles(test_smiles)
        self.assertEqual(test_molecule.mol_text, test_smiles,
                         "Expected mol_text attribute to be set "
                         "to smiles string")
        self.assertIsNotNone(test_molecule.mol_graph,
                             "Expected mol_graph attribute to be set "
                             "from the smiles")
        self.assertIsInstance(test_molecule.mol_graph, rdkit.Chem.rdchem.Mol,
                              "Expected initialized mol_graph to "
                              "be rdkit.Chem.rdchem.Mol object")

    def test_set_molecule_from_file(self):
        """
        Test to create Molecule object by reading the contents of a file.

        Case #1: text file
        Case #2: PDB file

        """
        test_smiles = 'CC'
        # Case 1: text file
        test_text_molecule = Molecule()
        text_fpath = 'test_mol_src.txt'
        print(f'Creating file {text_fpath}...')
        with open(text_fpath, "w") as fp:
            fp.write(test_smiles+' garbage vals')
        test_text_molecule._set_molecule_from_file(text_fpath)
        self.assertEqual(test_text_molecule.mol_text, test_smiles,
                         'Expected mol_text attribute to be set '
                         'to smiles string when loading from txt file')
        self.assertIsNotNone(test_text_molecule.mol_graph,
                             'Expected mol_graph attribute to be set '
                             'from the smiles when loading from txt file')
        self.assertIsInstance(test_text_molecule.mol_graph,
                              rdkit.Chem.rdchem.Mol,
                              'Expected initialized mol_graph to '
                              'be rdkit.Chem.rdchem.Mol object '
                              'when loading from txt file')
        print(f'Test complete. Deleting file {text_fpath}...')
        remove(text_fpath)

        # Case 2: pdb file
        test_pdb_molecule = Molecule()
        test_pdb_filename = 'test_mol_src.pdb'
        print(f'Creating file {test_pdb_filename}...')
        test_mol = MolFromSmiles(test_smiles)
        MolToPDBFile(test_mol, test_pdb_filename)
        test_pdb_molecule._set_molecule_from_file(test_pdb_filename)
        self.assertEqual(test_pdb_molecule.mol_text,
                         os.path.basename(test_pdb_filename).split('.')[0],
                         'Expected mol_text attribute to be set '
                         'to smiles string when loading from pdb file')
        self.assertIsNotNone(test_pdb_molecule.mol_graph,
                             'Expected mol_graph attribute to be set '
                             'from the smiles when loading from pdb file')
        self.assertIsInstance(test_pdb_molecule.mol_graph,
                              rdkit.Chem.rdchem.Mol,
                              'Expected initialized mol_graph to '
                              'be rdkit.Chem.rdchem.Mol object '
                              'when loading from pdb file')
        print(f'Test complete. Deleting file {test_pdb_filename}...')
        remove(test_pdb_filename)
    
    def test_molecule_draw(self):
        """
        Test to draw molecule stored in Molecule object.

        """
        test_smiles = 'CC'
        test_molecule = Molecule()
        test_molecule._set_molecule_from_smiles(test_smiles)
        test_image_fpath = test_smiles + '.png'
        test_molecule.draw(fpath=test_image_fpath)
        self.assertTrue(os.path.isfile(test_image_fpath))
        try:
            print(f'Deleting {test_image_fpath}')
            remove(test_image_fpath)
        except FileNotFoundError:
            print(f'Could not find {test_image_fpath}')

    def test_molecule_graph_similar_to_itself_morgan_tanimoto(self):
        """
        Test that the morgan fingerprint of a Molecule object is similar 
        to itself using Tanimoto similarity.

        """
        test_smiles = 'CC'
        fingerprint_type = 'morgan_fingerprint'
        similarity_metric = 'tanimoto'
        test_molecule = Molecule()
        test_molecule._set_molecule_from_smiles(test_smiles)
        test_molecule_duplicate = Molecule()
        test_molecule_duplicate._set_molecule_from_smiles(test_smiles)
        test_molecule.set_descriptor(fingerprint_type=fingerprint_type)
        test_molecule_duplicate.set_descriptor(
                                              fingerprint_type=fingerprint_type)
        similarity_measure = SimilarityMeasure(metric=similarity_metric)
        tanimoto_similarity = test_molecule.get_similarity_to_molecule(
                                     test_molecule_duplicate,
                                     similarity_measure=similarity_measure)
        self.assertEqual(tanimoto_similarity, 1.,
                         'Expected tanimoto similarity to be 1 when comparing '
                         'molecule graph to itself')

    def test_molecule_graph_similar_to_itself_morgan_negl0(self):
        """
        Test that the morgan fingerprint of a Molecule object is similar 
        to itself using negative L0 norm similarity.

        """
        test_smiles = 'CC'
        fingerprint_type = 'morgan_fingerprint'
        similarity_metric = 'negative_l0'
        test_molecule = Molecule()
        test_molecule._set_molecule_from_smiles(test_smiles)
        test_molecule_duplicate = Molecule()
        test_molecule_duplicate._set_molecule_from_smiles(test_smiles)
        test_molecule.set_descriptor(fingerprint_type=fingerprint_type)
        test_molecule_duplicate.set_descriptor(
                                              fingerprint_type=fingerprint_type)
        similarity_measure = SimilarityMeasure(metric=similarity_metric)
        negl0_similarity = test_molecule.get_similarity_to_molecule(
                                     test_molecule_duplicate,
                                     similarity_measure=similarity_measure)
        self.assertEqual(negl0_similarity, 0.,
                         'Expected negative L0 norm to be 0 when comparing '
                         'molecule graph to itself')

    def test_molecule_graph_similar_to_itself_morgan_dice(self):
        """
        Test that the morgan fingerprint of a Molecule object is similar 
        to itself using dice similarity.

        """
        test_smiles = 'CCO'
        fingerprint_type = 'morgan_fingerprint'
        similarity_metric = 'dice'
        test_molecule = Molecule()
        test_molecule._set_molecule_from_smiles(test_smiles)
        test_molecule_duplicate = Molecule()
        test_molecule_duplicate._set_molecule_from_smiles(test_smiles)
        test_molecule.set_descriptor(fingerprint_type=fingerprint_type)
        test_molecule_duplicate.set_descriptor(
                                              fingerprint_type=fingerprint_type)
        similarity_measure = SimilarityMeasure(metric=similarity_metric)
        dice_similarity = test_molecule.get_similarity_to_molecule(
                                     test_molecule_duplicate,
                                     similarity_measure=similarity_measure)
        self.assertEqual(dice_similarity, 1.,
                         'Expected dice similarity to be 1 when comparing '
                         'molecule graph to itself')


class TestMoleculeSet(unittest.TestCase):
    test_smiles = ['C', 'CC', 'CCC', 'O']
    
    def smiles_seq_to_textfile(self, property_seq=None):
        text_fpath = 'temp_smiles_seq.txt'
        print(f'Creating text file {text_fpath}')
        with open(text_fpath, "w") as fp:
            for id, smiles in enumerate(self.test_smiles):
                write_txt = smiles
                if property_seq is not None:
                    write_txt += ' ' + str(property_seq[id])
                if id < len(self.test_smiles) - 1:
                    write_txt += '\n'

                fp.write(write_txt)
        return text_fpath
    
    def smiles_seq_to_pdb_dir(self, property_seq=None):
        dir_path = 'test_dir'
        if not os.path.isdir(dir_path):
            print(f'Creating directory {dir_path}')
            mkdir(dir_path)
        for smiles_str in self.test_smiles:
            mol_graph = MolFromSmiles(smiles_str)
            assert mol_graph is not None
            pdb_fpath = os.path.join(dir_path, smiles_str + '.pdb')
            print(f'Creating file {pdb_fpath}')
            MolToPDBFile(mol_graph, pdb_fpath)
        return dir_path
    
    def smiles_seq_to_xl_or_csv(self,
                                ftype,
                                property_seq=None,
                                name_seq=None,
                                feature_arr=None):
        data = {'feature_smiles': self.test_smiles}
        if property_seq is not None:
            data.update({'response_random': property_seq})
        if name_seq is not None:
            data.update({'feature_name': name_seq})
        if feature_arr is not None:
            feature_arr = np.array(feature_arr)
            for feature_num in range(feature_arr.shape[1]):
                data.update({
                    f'feature_{feature_num}': feature_arr[:, feature_num]})
        data_df = pd.DataFrame(data)
        fpath = 'temp_mol_file'        
        if ftype == 'excel':
            fpath += '.xlsx'
            print(f'Creating {ftype} file {fpath}')
            data_df.to_excel(fpath)
        elif ftype == 'csv':
            fpath += '.csv'
            print(f'Creating {ftype} file {fpath}')
            data_df.to_csv(fpath)
        else:
            raise ValueError(f'{ftype} not supported')
        return fpath
                
    def test_set_molecule_database_from_textfile(self):
        text_fpath = self.smiles_seq_to_textfile()
        molecule_set = MoleculeSet(molecule_database_src=text_fpath,
                                   molecule_database_src_type='text',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from text')
        self.assertEqual(len(molecule_set.molecule_database), 
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles in text file')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles')
            self.assertIsNone(molecule.mol_property_val,
                              'Expected mol_property_val of Molecule object '
                              'initialized without property to be None')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {text_fpath}...')
        remove(text_fpath)

    def test_subsample_molecule_database_from_textfile(self):
        text_fpath = self.smiles_seq_to_textfile()
        sampling_ratio = 0.5
        molecule_set = MoleculeSet(molecule_database_src=text_fpath,
                                   molecule_database_src_type='text',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True,
                                   sampling_ratio=sampling_ratio)
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from text')
        self.assertEqual(len(molecule_set.molecule_database),
                         int(sampling_ratio * len(self.test_smiles)),
                         'Expected the size of subsampled database to be equal '
                         'to number of smiles in text file * sampling_ratio')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {text_fpath}...')
        remove(text_fpath)
    
    def test_set_molecule_database_w_property_from_textfile(self):
        properties = np.random.normal(size=len(self.test_smiles))
        text_fpath = self.smiles_seq_to_textfile(property_seq=properties)
        molecule_set = MoleculeSet(molecule_database_src=text_fpath,
                                   molecule_database_src_type='text',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from text')
        self.assertEqual(len(molecule_set.molecule_database), 
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles in text file')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles')
            self.assertAlmostEqual(molecule.mol_property_val, 
                                   properties[id],
                                   places=7,
                                   msg='Expected mol_property_val of' 
                                       'Molecule object '
                                       'to be set to value in text file')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {text_fpath}...')
        remove(text_fpath)
    
    def test_set_molecule_database_from_pdb_dir(self):
        dir_path = self.smiles_seq_to_pdb_dir(self.test_smiles)
        molecule_set = MoleculeSet(molecule_database_src=dir_path,
                                   molecule_database_src_type='directory',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from dir')
        self.assertEqual(len(molecule_set.molecule_database), 
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of files in dir')
        for molecule in molecule_set.molecule_database:
            self.assertIn(molecule.mol_text, self.test_smiles,
                          'Expected molecule text to be a smiles string')
            self.assertIsNone(molecule.mol_property_val,
                              'Expected mol_property_val of Molecule object'
                              'initialized without property to be None')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting directory {dir_path}...')
        rmtree(dir_path)

    def test_subsample_molecule_database_from_pdb_dir(self):
        dir_path = self.smiles_seq_to_pdb_dir(self.test_smiles)
        sampling_ratio = 0.5
        molecule_set = MoleculeSet(molecule_database_src=dir_path,
                                   molecule_database_src_type='directory',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True,
                                   sampling_ratio=sampling_ratio)
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from dir')
        self.assertEqual(len(molecule_set.molecule_database),
                         int(sampling_ratio * len(self.test_smiles)),
                         'Expected the size of subsampled database to be '
                         'equal to number of files in dir * sampling_ratio')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting directory {dir_path}...')
        rmtree(dir_path)

    def test_set_molecule_database_from_excel(self):
        xl_fpath = self.smiles_seq_to_xl_or_csv(ftype='excel')
        molecule_set = MoleculeSet(molecule_database_src=xl_fpath,
                                   molecule_database_src_type='excel',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'excel file')
        self.assertEqual(len(molecule_set.molecule_database), 
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles when names not present in excel')
            self.assertIsNone(molecule.mol_property_val,
                              'Expected mol_property_val of Molecule object'
                              'initialized without property to be None')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {xl_fpath}...')
        remove(xl_fpath)

    def test_subsample_molecule_database_from_excel(self):
        xl_fpath = self.smiles_seq_to_xl_or_csv(ftype='excel')
        sampling_ratio = 0.5
        molecule_set = MoleculeSet(molecule_database_src=xl_fpath,
                                   molecule_database_src_type='excel',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True,
                                   sampling_ratio=sampling_ratio)
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'excel file')
        self.assertEqual(len(molecule_set.molecule_database),
                         int(sampling_ratio * len(self.test_smiles)),
                         'Expected the size of subsampled database to be '
                         'equal to number of smiles * sampling ratio')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {xl_fpath}...')
        remove(xl_fpath)
    
    def test_set_molecule_database_w_property_from_excel(self):
        properties = np.random.normal(size=len(self.test_smiles))
        xl_fpath = self.smiles_seq_to_xl_or_csv(ftype='excel', 
                                                property_seq=properties)
        molecule_set = MoleculeSet(molecule_database_src=xl_fpath,
                                   molecule_database_src_type='excel',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'excel file')
        self.assertEqual(len(molecule_set.molecule_database), 
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles in excel file')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles when names not present in excel')
            self.assertAlmostEqual(molecule.mol_property_val, 
                                   properties[id],
                                   places=7,
                                   msg='Expected mol_property_val of' 
                                       'Molecule object '
                                       'to be set to value in excel file')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
            print(f'Test complete. Deleting file {xl_fpath}...')
        remove(xl_fpath)

    def test_set_molecule_database_w_descriptor_property_from_excel(self):
        properties = np.random.normal(size=len(self.test_smiles))
        n_features = 20
        features = np.random.normal(size=(len(self.test_smiles), n_features))
        xl_fpath = self.smiles_seq_to_xl_or_csv(ftype='excel',
                                                property_seq=properties,
                                                feature_arr=features)
        molecule_set = MoleculeSet(molecule_database_src=xl_fpath,
                                   molecule_database_src_type='excel',
                                   similarity_measure='negative_l0',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose,
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'excel file')
        self.assertEqual(len(molecule_set.molecule_database),
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles in excel file')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles when names not present in excel')
            self.assertAlmostEqual(molecule.mol_property_val,
                                   properties[id],
                                   places=7,
                                   msg='Expected mol_property_val of' 
                                       'Molecule object '
                                       'to be set to value in excel file')
            self.assertTrue((molecule.descriptor.to_numpy()
                             == features[id]).all,
                            'Expected descriptor value to be same as the '
                            'vector used to initialize descriptor')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
            print(f'Test complete. Deleting file {xl_fpath}...')
        remove(xl_fpath)

    def test_set_molecule_database_from_csv(self):
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv')
        molecule_set = MoleculeSet(molecule_database_src=csv_fpath,
                                   molecule_database_src_type='csv',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'csv file')
        self.assertEqual(len(molecule_set.molecule_database), 
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles when names not present in csv')
            self.assertIsNone(molecule.mol_property_val,
                              'Expected mol_property_val of Molecule object'
                              'initialized without property to be None')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)

    def test_subsample_molecule_database_from_csv(self):
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv')
        sampling_ratio = 0.5
        molecule_set = MoleculeSet(molecule_database_src=csv_fpath,
                                   molecule_database_src_type='csv',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   sampling_ratio=sampling_ratio,
                                   is_verbose=True)
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'csv file')
        self.assertEqual(len(molecule_set.molecule_database),
                         int(sampling_ratio * len(self.test_smiles)),
                         'Expected the size of database to be equal to number '
                         'of smiles * sampling_ratio')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
        print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)
    
    def test_set_molecule_database_w_property_from_csv(self):
        properties = np.random.normal(size=len(self.test_smiles))
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv', 
                                                 property_seq=properties)
        molecule_set = MoleculeSet(molecule_database_src=csv_fpath,
                                   molecule_database_src_type='csv',
                                   fingerprint_type='morgan_fingerprint',
                                   similarity_measure='tanimoto',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose, 
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'csv file')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles when names not present in csv')
            self.assertAlmostEqual(molecule.mol_property_val, 
                                   properties[id],
                                   places=7,
                                   msg='Expected mol_property_val of' 
                                       'Molecule object '
                                       'to be set to value in csv file')
            self.assertIsInstance(molecule, Molecule)
        print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)

    def test_set_molecule_database_w_descriptor_property_from_csv(self):
        properties = np.random.normal(size=len(self.test_smiles))
        n_features = 20
        features = np.random.normal(size=(len(self.test_smiles), n_features))
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv',
                                                 property_seq=properties,
                                                 feature_arr=features)
        molecule_set = MoleculeSet(molecule_database_src=csv_fpath,
                                   molecule_database_src_type='csv',
                                   similarity_measure='negative_l0',
                                   is_verbose=True)
        self.assertTrue(molecule_set.is_verbose,
                        'Expected is_verbose to be True')
        self.assertIsNotNone(molecule_set.molecule_database,
                             'Expected molecule_database to be set from '
                             'excel file')
        self.assertEqual(len(molecule_set.molecule_database),
                         len(self.test_smiles),
                         'Expected the size of database to be equal to number '
                         'of smiles in csv file')
        for id, molecule in enumerate(molecule_set.molecule_database):
            self.assertEqual(molecule.mol_text, self.test_smiles[id],
                             'Expected mol_text attribute of Molecule object '
                             'to be smiles when names not present in csv')
            self.assertAlmostEqual(molecule.mol_property_val,
                                   properties[id],
                                   places=7,
                                   msg='Expected mol_property_val of' 
                                       'Molecule object '
                                       'to be set to value in csv file')
            self.assertTrue((molecule.descriptor.to_numpy()
                             == features[id]).all,
                            'Expected descriptor value to be same as the '
                            'vector used to initialize descriptor')
            self.assertIsInstance(molecule, Molecule,
                                  'Expected member of molecule_set to '
                                  'be Molecule object')
            print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)

    def test_set_molecule_database_w_similarity_from_csv(self):
        properties = np.random.normal(size=len(self.test_smiles))
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv', 
                                                 property_seq=properties)
        for similarity_measure in SUPPORTED_SIMILARITIES:
            with self.assertRaises(NotInitializedError):
                MoleculeSet(
                    molecule_database_src=csv_fpath,
                    molecule_database_src_type='csv',
                    similarity_measure=similarity_measure,
                    is_verbose=True)

        print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)
    
    def test_set_molecule_database_fingerprint_from_csv(self):
        properties = np.random.normal(size=len(self.test_smiles))
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv', 
                                                 property_seq=properties)
        for descriptor in SUPPORTED_FPRINTS:
            with self.assertRaises(TypeError):
                MoleculeSet(
                    molecule_database_src=csv_fpath,
                    molecule_database_src_type='csv',
                    fingerprint_type=descriptor,
                    is_verbose=True)

        print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)
    
    def test_set_molecule_database_w_fingerprint_similarity_from_csv(self):
        properties = np.random.normal(size=len(self.test_smiles))
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv', 
                                                 property_seq=properties)
        for descriptor in SUPPORTED_FPRINTS:
            for similarity_measure in SUPPORTED_SIMILARITIES:
                molecule_set = MoleculeSet(
                                        molecule_database_src=csv_fpath,
                                        molecule_database_src_type='csv',
                                        fingerprint_type=descriptor,
                                        similarity_measure=similarity_measure,
                                        is_verbose=True)
                self.assertTrue(molecule_set.is_verbose, 
                                'Expected is_verbose to be True')
                self.assertIsNotNone(molecule_set.molecule_database,
                                     'Expected molecule_database to '
                                     'be set from csv file')
                for molecule in molecule_set.molecule_database:
                    self.assertTrue(molecule.descriptor.check_init(),
                                    'Expected descriptor to be set')
                self.assertIsNotNone(molecule_set.similarity_matrix,
                                     'Expected similarity_matrix to be set')
        print(f'Test complete. Deleting file {csv_fpath}...')
        remove(csv_fpath)
    
    def test_get_most_similar_pairs(self):
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv')
        for descriptor in SUPPORTED_FPRINTS:
            for similarity_measure in SUPPORTED_SIMILARITIES:
                molecule_set = MoleculeSet(
                                       molecule_database_src=csv_fpath,
                                       molecule_database_src_type='csv',
                                       fingerprint_type=descriptor,
                                       similarity_measure=similarity_measure,
                                       is_verbose=True)
                molecule_pairs = molecule_set.get_most_similar_pairs()
                self.assertIsInstance(molecule_pairs, list, 
                                      'Expected get_most_similar_pairs() '
                                      'to return list')
                for pair in molecule_pairs:
                    self.assertIsInstance(pair, tuple, 
                                          'Expected elements of list '
                                          'returned by get_most_similar_pairs()'
                                          ' to be tuples')
    
    def test_get_most_dissimilar_pairs(self):
        csv_fpath = self.smiles_seq_to_xl_or_csv(ftype='csv')
        for descriptor in SUPPORTED_FPRINTS:
            for similarity_measure in SUPPORTED_SIMILARITIES:
                molecule_set = MoleculeSet(
                                        molecule_database_src=csv_fpath,
                                        molecule_database_src_type='csv',
                                        fingerprint_type=descriptor,
                                        similarity_measure=similarity_measure,
                                        is_verbose=True)
                molecule_pairs = molecule_set.get_most_dissimilar_pairs()
                self.assertIsInstance(molecule_pairs, list, 
                                      'Expected get_most_dissimilar_pairs() '
                                      'to return list')
                for pair in molecule_pairs:
                    self.assertIsInstance(pair, tuple, 
                                          'Expected elements of list returned'
                                          ' by get_most_dissimilar_pairs() '
                                          'to be tuples')


if __name__ == '__main__':
    unittest.main()
