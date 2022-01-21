Search.setIndex({docnames:["README","implemented_metrics","index","interfaces","interfaces.UI","modules","molSim","molSim.chemical_datastructures","molSim.ops","molSim.tasks","molSim.utils","setup","tests"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["README.rst","implemented_metrics.rst","index.rst","interfaces.rst","interfaces.UI.rst","modules.rst","molSim.rst","molSim.chemical_datastructures.rst","molSim.ops.rst","molSim.tasks.rst","molSim.utils.rst","setup.rst","tests.rst"],objects:{"":[[3,0,0,"-","interfaces"],[6,0,0,"-","molSim"],[12,0,0,"-","tests"]],"interfaces.config_reader":[[3,1,1,"","main"]],"molSim.chemical_datastructures":[[7,0,0,"-","molecule"],[7,0,0,"-","molecule_set"]],"molSim.chemical_datastructures.molecule":[[7,2,1,"","Molecule"]],"molSim.chemical_datastructures.molecule.Molecule":[[7,3,1,"","draw"],[7,3,1,"","get_descriptor_val"],[7,3,1,"","get_mol_property_val"],[7,3,1,"","get_name"],[7,3,1,"","get_similarity_to"],[7,3,1,"","is_same"],[7,3,1,"","match_fingerprint_from"],[7,3,1,"","set_descriptor"]],"molSim.chemical_datastructures.molecule_set":[[7,2,1,"","MoleculeSet"]],"molSim.chemical_datastructures.molecule_set.MoleculeSet":[[7,3,1,"","cluster"],[7,3,1,"","compare_against_molecule"],[7,3,1,"","get_cluster_labels"],[7,3,1,"","get_distance_matrix"],[7,3,1,"","get_mol_names"],[7,3,1,"","get_mol_properties"],[7,3,1,"","get_most_dissimilar_pairs"],[7,3,1,"","get_most_similar_pairs"],[7,3,1,"","get_pairwise_similarities"],[7,3,1,"","get_property_of_most_dissimilar"],[7,3,1,"","get_property_of_most_similar"],[7,3,1,"","get_similarity_matrix"],[7,3,1,"","get_transformed_descriptors"],[7,3,1,"","is_present"]],"molSim.exceptions":[[6,4,1,"","InvalidConfigurationError"],[6,4,1,"","LoadingError"],[6,4,1,"","MissingRDKitError"],[6,4,1,"","MordredCalculatorError"],[6,4,1,"","NotInitializedError"]],"molSim.ops":[[8,0,0,"-","clustering"],[8,0,0,"-","descriptor"],[8,0,0,"-","similarity_measures"]],"molSim.ops.clustering":[[8,2,1,"","Cluster"]],"molSim.ops.clustering.Cluster":[[8,3,1,"","fit"],[8,3,1,"","get_labels"],[8,3,1,"","predict"]],"molSim.ops.descriptor":[[8,2,1,"","Descriptor"]],"molSim.ops.descriptor.Descriptor":[[8,3,1,"","check_init"],[8,3,1,"","fold_to_equal_length"],[8,3,1,"","get_all_supported_descriptors"],[8,3,1,"","get_folded_fprint"],[8,3,1,"","get_label"],[8,3,1,"","get_params"],[8,3,1,"","get_supported_fprints"],[8,3,1,"","is_fingerprint"],[8,3,1,"","make_fingerprint"],[8,3,1,"","set_manually"],[8,3,1,"","shorten_label"],[8,3,1,"","to_numpy"],[8,3,1,"","to_rdkit"]],"molSim.ops.similarity_measures":[[8,2,1,"","SimilarityMeasure"]],"molSim.ops.similarity_measures.SimilarityMeasure":[[8,3,1,"","get_compatible_metrics"],[8,3,1,"","get_supported_binary_metrics"],[8,3,1,"","get_supported_general_metrics"],[8,3,1,"","get_supported_metrics"],[8,3,1,"","get_uniq_metrics"],[8,3,1,"","is_distance_metric"]],"molSim.tasks":[[9,0,0,"-","cluster_data"],[9,0,0,"-","compare_target_molecule"],[9,0,0,"-","identify_outliers"],[9,0,0,"-","measure_search"],[9,0,0,"-","see_property_variation_with_similarity"],[9,0,0,"-","task"],[9,0,0,"-","task_manager"],[9,0,0,"-","visualize_dataset"]],"molSim.tasks.cluster_data":[[9,2,1,"","ClusterData"]],"molSim.tasks.compare_target_molecule":[[9,2,1,"","CompareTargetMolecule"]],"molSim.tasks.compare_target_molecule.CompareTargetMolecule":[[9,3,1,"","get_hits_dissimilar_to"],[9,3,1,"","get_hits_similar_to"]],"molSim.tasks.identify_outliers":[[9,2,1,"","IdentifyOutliers"]],"molSim.tasks.measure_search":[[9,2,1,"","MeasureSearch"]],"molSim.tasks.measure_search.MeasureSearch":[[9,3,1,"","get_best_measure"]],"molSim.tasks.see_property_variation_with_similarity":[[9,2,1,"","SeePropertyVariationWithSimilarity"]],"molSim.tasks.see_property_variation_with_similarity.SeePropertyVariationWithSimilarity":[[9,3,1,"","get_property_correlations_in_most_dissimilar"],[9,3,1,"","get_property_correlations_in_most_similar"]],"molSim.tasks.task":[[9,2,1,"","Task"]],"molSim.tasks.task_manager":[[9,2,1,"","TaskManager"]],"molSim.tasks.visualize_dataset":[[9,2,1,"","VisualizeDataset"]],"molSim.utils":[[10,0,0,"-","ccbmlib_fingerprints"],[10,0,0,"-","plotting_scripts"]],"molSim.utils.ccbmlib_fingerprints":[[10,1,1,"","atom_pairs"],[10,1,1,"","avalon"],[10,1,1,"","generate_fingerprints"],[10,1,1,"","hash_parameter_set"],[10,1,1,"","hashed_atom_pairs"],[10,1,1,"","hashed_morgan"],[10,1,1,"","hashed_torsions"],[10,1,1,"","maccs_keys"],[10,1,1,"","morgan"],[10,1,1,"","rdkit_fingerprint"],[10,1,1,"","to_key_val_string"],[10,1,1,"","torsions"]],"molSim.utils.plotting_scripts":[[10,1,1,"","plot_barchart"],[10,1,1,"","plot_density"],[10,1,1,"","plot_heatmap"],[10,1,1,"","plot_multiple_barchart"],[10,1,1,"","plot_parity"],[10,1,1,"","plot_scatter"]],"tests.test_CompareTargetMolecule":[[12,2,1,"","TestCompareTargetMolecule"],[12,1,1,"","test_get_molecule_least_similar_to"]],"tests.test_CompareTargetMolecule.TestCompareTargetMolecule":[[12,3,1,"","smiles_seq_to_xl_or_csv"],[12,3,1,"","test_get_molecule_most_similar_to"]],"tests.test_Descriptor":[[12,2,1,"","TestDescriptor"]],"tests.test_Descriptor.TestDescriptor":[[12,3,1,"","test_descriptor_arbitrary_list_init"],[12,3,1,"","test_descriptor_arbitrary_numpy_init"],[12,3,1,"","test_descriptor_empty_init"],[12,3,1,"","test_descriptor_make_fingerprint"],[12,3,1,"","test_fingerprint_folding"],[12,3,1,"","test_mordred_descriptors"],[12,3,1,"","test_nonexistent_mordred_descriptors"],[12,3,1,"","test_topological_fprint_min_path_lesser_than_atoms"]],"tests.test_Molecule":[[12,2,1,"","TestMolecule"]],"tests.test_Molecule.TestMolecule":[[12,3,1,"","test_mol_mol_similarity_w_morgan_tanimoto"],[12,3,1,"","test_molecule_created_w_attributes"],[12,3,1,"","test_molecule_created_with_no_attributes"],[12,3,1,"","test_molecule_draw"],[12,3,1,"","test_molecule_graph_similar_to_itself_morgan_dice"],[12,3,1,"","test_molecule_graph_similar_to_itself_morgan_l0"],[12,3,1,"","test_molecule_graph_similar_to_itself_morgan_tanimoto"],[12,3,1,"","test_set_molecule_from_file"],[12,3,1,"","test_set_molecule_from_smiles"]],"tests.test_MoleculeSet":[[12,2,1,"","TestMoleculeSet"]],"tests.test_MoleculeSet.TestMoleculeSet":[[12,3,1,"","smarts_seq_to_smiles_file"],[12,3,1,"","smiles_seq_to_pdb_dir"],[12,3,1,"","smiles_seq_to_smi_file"],[12,3,1,"","smiles_seq_to_smiles_file"],[12,3,1,"","smiles_seq_to_textfile"],[12,3,1,"","smiles_seq_to_xl_or_csv"],[12,3,1,"","test_clustering_fingerprints"],[12,3,1,"","test_get_most_dissimilar_pairs"],[12,3,1,"","test_get_most_similar_pairs"],[12,3,1,"","test_pca_transform"],[12,3,1,"","test_set_molecule_database_fingerprint_from_csv"],[12,3,1,"","test_set_molecule_database_from_csv"],[12,3,1,"","test_set_molecule_database_from_excel"],[12,3,1,"","test_set_molecule_database_from_pdb_dir"],[12,3,1,"","test_set_molecule_database_from_smarts_file"],[12,3,1,"","test_set_molecule_database_from_smi_file"],[12,3,1,"","test_set_molecule_database_from_smiles_file"],[12,3,1,"","test_set_molecule_database_from_textfile"],[12,3,1,"","test_set_molecule_database_w_descriptor_property_from_csv"],[12,3,1,"","test_set_molecule_database_w_descriptor_property_from_excel"],[12,3,1,"","test_set_molecule_database_w_fingerprint_similarity_from_csv"],[12,3,1,"","test_set_molecule_database_w_property_from_csv"],[12,3,1,"","test_set_molecule_database_w_property_from_excel"],[12,3,1,"","test_set_molecule_database_w_property_from_textfile"],[12,3,1,"","test_set_molecule_database_w_similarity_from_csv"],[12,5,1,"","test_smarts"],[12,5,1,"","test_smiles"],[12,3,1,"","test_subsample_molecule_database_from_csv"],[12,3,1,"","test_subsample_molecule_database_from_excel"],[12,3,1,"","test_subsample_molecule_database_from_pdb_dir"],[12,3,1,"","test_subsample_molecule_database_from_textfile"]],"tests.test_SimilarityMeasure":[[12,2,1,"","TestSimilarityMeasure"]],"tests.test_SimilarityMeasure.TestSimilarityMeasure":[[12,3,1,"","smiles_seq_to_xl_or_csv"],[12,3,1,"","test_all_supported_measures"],[12,3,1,"","test_get_abcd"],[12,3,1,"","test_similarity_measure_limits"]],"tests.test_multithreading":[[12,2,1,"","TestMultithreading"]],"tests.test_multithreading.TestMultithreading":[[12,3,1,"","setUpClass"],[12,3,1,"","tearDownClass"],[12,3,1,"","test_multithreading_consistency_10_threads"],[12,3,1,"","test_multithreading_consistency_2_threads"],[12,3,1,"","test_multithreading_consistency_3_threads"],[12,3,1,"","test_multithreading_consistency_4_threads"],[12,3,1,"","test_multithreading_consistency_5_threads"],[12,3,1,"","test_multithreading_consistency_6_threads"],[12,3,1,"","test_multithreading_consistency_7_threads"],[12,3,1,"","test_speedup_efficiency_cosine"],[12,3,1,"","test_speedup_efficiency_tanimoto"]],interfaces:[[4,0,0,"-","UI"],[3,0,0,"-","config_reader"]],molSim:[[7,0,0,"-","chemical_datastructures"],[6,0,0,"-","exceptions"],[8,0,0,"-","ops"],[9,0,0,"-","tasks"],[10,0,0,"-","utils"]],tests:[[12,0,0,"-","test_CompareTargetMolecule"],[12,0,0,"-","test_Descriptor"],[12,0,0,"-","test_Molecule"],[12,0,0,"-","test_MoleculeSet"],[12,0,0,"-","test_SimilarityMeasure"],[12,0,0,"-","test_multithreading"]]},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","method","Python method"],"4":["py","exception","Python exception"],"5":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:method","4":"py:exception","5":"py:attribute"},terms:{"0":[7,9,10,12],"01":9,"1":[0,7,10,12],"10":[0,12],"1002":0,"1021":0,"1038":0,"11":12,"140":0,"1669":0,"2":[0,10,12],"20":10,"2005":0,"2009":0,"2011":0,"2013":0,"2018":0,"24":10,"28":0,"2nd":0,"3":[0,12],"4":[0,12],"42":7,"44":0,"5":[0,12],"5000":0,"53":0,"597":0,"6":[0,12],"601":0,"7":[0,12],"8":[0,7,12],"8781":0,"8787":0,"8b04532":0,"9":12,"abstract":[7,9],"case":[0,7,10,12],"class":[6,7,8,9,12],"default":[7,8,9,10,12],"do":0,"float":[7,9],"function":[10,12],"int":[7,8,9,10],"new":0,"return":[7,8,9,10,12],"static":[7,8],"true":[7,8,9],"try":[0,7],A:[0,7],For:0,If:[0,3,7,9,10],In:0,Or:0,The:[0,7,8,9],There:0,To:[0,10],_build:0,_can_:8,_fingerprint:8,abc:9,abil:12,about:0,abov:0,absenc:7,absolut:9,accord:0,account:0,across:0,activ:0,addit:[0,7],addition:0,against:0,aggress:9,aka:8,al:9,algorithm:[0,7,9],alias:1,all:[0,7,8,9,12],alogirthm:0,along:[0,10],alreadi:0,also:0,alt:0,altern:0,although:9,am:0,an:[0,3,6,7,9,12],analysi:[7,12],ani:0,annot:10,anoth:[0,7],apidoc:0,appar:0,appear:0,applic:0,approach:12,appropri:[0,9],ar:[0,7,8,9,10,12],arbitrari:[0,7,8,12],arbitrary_descriptor_v:[7,8],arg:[7,8,9,10,12],argument:[7,8,10],arrai:[7,8,10,12],assess:0,associ:0,atom_pair:10,attempt:6,attribut:[7,12],attributeerror:6,autom:0,avail:0,avalon:10,averag:0,avoid:0,axi:10,b:[7,12],back:8,badge_logo:0,bar:10,base:[0,6,7,8,9,12],becaus:[0,7],becom:0,behavior:12,being:8,below:0,best:9,better:9,between:[0,7,8,9],bhattacharje:0,binari:[0,8],binder:0,bit:8,bool:[7,8,9,10],borg:0,both:9,branch:0,breviti:9,broken:7,browser:0,build:0,burn:0,bz2:0,c1:12,c:[0,12],calcul:[6,7,9],call:[0,3,6,8,9],campaign:0,can:[0,9,10,12],cannot:6,carri:9,categori:10,cc1:12,cc:12,ccbmlib:0,ccbmlib_fingerprint:[5,6],ccc:12,cccc:12,ccccccc:12,cdatastruct:8,ch2:12,ch3:12,ch:12,chart:10,check:[0,7,8,12],check_init:8,chem:0,chemic:0,chemical_datastructur:[5,6,9],chemist:0,chen:0,choic:9,choos:0,chosen:[0,7,9],cite:2,classmethod:12,closest:7,cluster:[0,5,6,7,9,12],cluster_data:[5,6],cluster_grouped_mol_nam:7,clusterdata:9,clustering_method:[7,8],cn:12,co:12,coeffici:7,collect:7,collin:0,color:10,combin:12,combinatori:9,command:[0,3],common:10,commonli:0,compar:[0,7],compare_against_molecul:7,compare_target_molecul:[5,6],comparetargetmolecul:[9,12],comparison:[0,12],complet:0,complex:[8,12],compon:[0,12],comprehens:0,compris:7,comptabil:8,config:[0,9],config_read:5,configur:[3,6,9],consid:8,consist:12,constraint:1,consum:0,contain:[8,12],content:5,context:0,contrera:0,control:7,convers:0,convert:[8,9,12],core:0,correl:[0,9],correspond:9,cost:0,coupl:0,cp:0,cpu:0,creat:[0,9,12],creation:12,credit:2,csv:12,current:8,d:0,data:[0,7,9],databas:[0,9,12],dataset:[0,7,9],datastruct:8,davi:0,daylight:0,decreas:9,defin:[0,7,9],delet:12,demo:0,denot:[8,12],densiti:[0,10],depend:0,desciptornam:0,descriptor:[0,5,6,7,12],descriptornam:0,design:0,desir:0,destroi:0,detect:0,determin:7,develop:0,diagon:0,dice:12,dict:[7,8,9,10],dictionari:[7,8],differ:[0,10],dimens:0,dimension:0,directli:0,directori:[0,12],discov:0,displai:7,dissimilar:[0,7,9],dist:[0,1],distanc:[0,1,7,8,9],divers:0,doc:0,doi:0,don:[0,7],draw:[7,12],drug:0,due:[0,9],duplic:7,dure:7,e:[7,9],each:[0,7,8,10],ecfp:0,ed:0,effici:0,efficieni:12,effort:0,element:0,empti:[3,12],enough:0,ensur:[0,12],entir:0,env:0,environ:0,equal:[8,10],equival:0,essenti:0,etc:10,euclidean:0,evalu:[0,9,12],everyth:0,exampl:0,excel:12,except:[5,9],exclud:8,execut:[0,12],exist:0,experiment:[0,8],explicitbitvect:8,exploratori:0,explos:9,f:0,fail:[6,7],fals:[9,10],featur:[0,8,9,12],feature_arr:12,field:[3,9],file:[0,3,7,12],filenam:0,filetyp:12,find:[0,8,12],fingerprint1:8,fingerprint2:8,fingerprint:[7,8,9,12],fingerprint_param:[7,8],fingerprint_typ:[7,8,9,12],first:[0,7,10],fit:8,fix:9,fold:[8,12],fold_to_equal_length:8,fold_to_length:8,follow:0,fontsiz:10,forest:0,form:[0,9],format:8,formula:1,fp:[8,10],fpath:7,fraction:[7,9],friedman:0,from:[0,3,7,8,9,12],ftype:12,further:0,furthest:[0,9],furthest_neighbor_correl:9,gener:0,generate_fingerprint:10,generate_similarity_matrix:7,get:[7,8,9],get_all_supported_descriptor:8,get_best_measur:9,get_cluster_label:7,get_compatible_metr:8,get_descriptor_v:7,get_distance_matrix:7,get_folded_fprint:8,get_hits_dissimilar_to:9,get_hits_similar_to:9,get_label:8,get_mol_nam:7,get_mol_properti:7,get_mol_property_v:7,get_molecule_least_similar_to:12,get_most_dissimilar_pair:[7,12],get_most_similar_pair:[7,12],get_nam:7,get_pairwise_similar:7,get_param:8,get_property_correlations_in_most_dissimilar:9,get_property_correlations_in_most_similar:9,get_property_of_most_dissimilar:7,get_property_of_most_similar:7,get_similarity_matrix:7,get_similarity_to:7,get_supported_binary_metr:8,get_supported_descriptor:8,get_supported_fprint:8,get_supported_general_metr:8,get_supported_metr:8,get_transformed_descriptor:7,get_uniq_metr:8,gh:0,give:0,gloriu:0,good:0,graph:[7,8,12],graphic:0,grid:10,groenen:0,group:0,ha:7,halid:0,hash_parameter_set:10,hashed_atom_pair:10,hashed_morgan:10,hashed_tors:10,hasti:0,have:[7,9],he:9,heatmap:[0,10],height:10,help:0,helper:12,heteratom:0,hierarch:0,high:0,highest:9,himaghna:0,hour:0,how:7,html:0,http:0,i:[0,7,9],id:[7,9],idea:0,ident:12,identifi:[0,9],identify_outli:[5,6],identifyoutli:9,imag:[0,7],implement:[8,9,12],in_dtyp:8,includ:0,index:[2,7],indic:[0,7,9,10],infer:0,inform:[0,7],initi:[6,12],input:[0,3,8,10],input_matrix:10,instal:[2,6],instanti:12,instead:0,interest:[0,9],interfac:[0,2,5],invalid:[6,12],invalidconfigurationerror:[6,8,10],invok:8,io:7,ioerror:3,ipynb:0,is_distance_metr:8,is_fingerprint:8,is_pres:7,is_sam:7,is_verbos:7,isol:0,isolationforest:9,iter:0,its:[0,9],itself:12,j:0,jac:0,jackson:0,jacksonburn:0,just:10,k:0,keep:7,kei:7,keyword:[7,8,10],knowl:0,kwarg:[7,8,9,10],l0:[0,12],l1:0,l2:0,lab:0,label:[7,8,9,10,12],label_:8,labori:0,labpath:0,larger:0,lead:0,learn:0,least:7,legend:10,legend_label:10,length:8,less:10,librari:0,licens:2,line:[0,3],linkag:0,linkedin:0,list:[0,7,8,9,10,12],load:[6,12],loadingerror:6,longer:8,look:9,m2r:0,m:0,maccs_kei:10,machin:0,mai:[0,7],main:3,make:[0,8],make_fingerprint:8,mani:0,manipul:7,manual:[0,8],master:0,match_fingerprint_from:7,matric:12,matrix:[7,8,10,12],max:9,max_min:9,maxim:[0,9],md:0,measur:[0,7,8,9,12],measure_search:[5,6],measuresearch:9,medoid:0,messag:6,method:[7,8,12],method_:7,methodnam:12,metric:[0,2,7,8,9,12],might:0,min:9,mine:0,minim:[0,9],missingrdkiterror:6,mit:0,model:[0,8],modern:0,modifi:[7,8,10],modul:[2,5],moieti:0,mol:[7,10],mol_descriptor_v:7,mol_graph:7,mol_property_v:7,mol_smil:7,mol_src:7,mol_suppl:10,mol_text:7,molecul:[0,5,6,8,9,12],molecular:[0,7,8,12],molecule_databas:7,molecule_database_src:7,molecule_database_src_typ:7,molecule_graph:8,molecule_set:[5,6,9],molecule_set_config:9,moleculeset:[7,9,12],moleculset:12,molsim:[3,12],molsim_ui_main:[3,5],mordr:[0,6,12],mordredcalculatorerror:6,more:[0,9,10,12],morgan:[0,10,12],most:[0,7,9],much:7,multi:0,multidimension:0,multipl:[0,7,9,10],multiplear:10,multiprocess:[0,12],multithread:12,murrai:0,murtagh:0,mv:0,mybind:0,n:[10,12],n_bar:10,n_bars_per_xtick:10,n_cluster:[7,8],n_densiti:10,n_mol:7,n_points_per_dens:10,n_thread:7,n_worker:0,n_xtick:10,name:[0,1,7,10,12],name_seq:12,namedtupl:9,natur:0,nbsp:0,nchem:0,ndarrai:[7,8,9,10,12],nearest:[0,9],nearest_neighbor_correl:9,need:[0,9],neighbor:[0,9],newli:0,nh:12,non:7,none:[6,7,8,9,10,12],norm:[0,12],note:[0,7,8],notinitializederror:[6,7,12],novel:0,np:[7,8,9,10,12],num_hit:9,number:[0,7,8,10],numpi:[7,8,10,12],numpy_:8,o:[0,12],object:[6,7,8,9,12],often:0,oh:12,onc:0,one:[0,7,8,10],ones:[0,10],onli:[0,8,9],onlin:0,only_metr:9,op:[5,6,7],open:0,oper:0,optim:[0,9],optim_algo:9,option:[9,10,12],order:9,org:0,oserror:6,other:[7,8],our:0,out:9,outlier:[0,9],outlier_idx:10,output:[0,6],over:[0,9],overal:9,overview:0,p:0,packag:[0,2,5],pair:[0,7],pairwis:[0,7],par:10,paramet:[6,7,8,9],parent:9,pariti:10,parti:0,partner:0,pass:[10,12],passthrough:12,path:[0,7,12],pattern:0,pca:7,pdb:12,per:10,perform:9,person:0,pharmocolog:0,plot:[0,7,8,9,10],plot_barchart:10,plot_dens:10,plot_heatmap:10,plot_multiple_barchart:10,plot_par:10,plot_scatt:10,plot_titl:10,plot_title_fonts:10,plotting_script:[5,6],potenti:0,pr:0,practic:0,predict:[0,8],present:7,princip:12,probabl:0,process:[0,12],produc:12,project:0,proper:6,properti:[0,6,7,9],property_seq:12,propos:0,provid:0,purpos:[2,8],push:0,py:6,pypi:0,pyplot:10,python:[0,12],qoi:0,qualiti:0,quantiti:9,queri:[7,9],query_molecul:[7,9],r:0,rais:[3,7,8,10,12],randomli:[7,12],rapid:0,rare:8,rdkit:[0,6,7,8],rdkit_:8,rdkit_fingerprint:10,reaction:0,read:[3,12],readm:2,realiti:0,reccomend:0,recommend:9,redund:[0,8],refer:[0,7],reference_mol:7,region:0,relev:7,remov:8,repertoir:0,replic:0,repres:[8,10],represent:8,requir:0,research:0,respect:7,respons:[9,12],result:0,robust:0,roger:1,rst:0,run:[2,12],runtest:12,runtimeerror:6,s:[0,7,8,10,12],same:[0,7],sampl:[7,10],sample_ratio:9,sampling_random_st:7,sampling_ratio:7,satisfi:9,scalar:12,scale:0,scatter:10,scheme:0,scope:0,score:[7,9],score_:9,screen:0,search:[0,7],second:[7,10],see:[0,7],see_property_variation_with_similar:[5,6],seepropertyvariationwithsimilar:9,select:[0,9],self:[7,9,12],separ:[0,9],sequenc:[9,12],seri:[0,10],serial:12,set:[0,7,8,9,10],set_descriptor:7,set_manu:8,set_molecul:9,set_similar:7,setup:[2,5],setupclass:12,sever:0,shade:10,shape:10,shortcom:0,shorten:8,shorten_label:8,should:0,show_plot:10,shown:0,similar:[2,7,8,9,10,12],similarity_matrix:7,similarity_measur:[5,6,7,9,12],similarity_scor:7,similaritymeasur:[7,8,12],sinc:[7,9],singl:[0,12],site:0,size:[8,10],smaller:[0,8],smart:12,smarts_seq_to_smiles_fil:12,smi:12,smile:12,smiles_seq_to_pdb_dir:12,smiles_seq_to_smi_fil:12,smiles_seq_to_smiles_fil:12,smiles_seq_to_textfil:12,smiles_seq_to_xl_or_csv:12,soc:0,solvent:0,some:10,sort:9,sorted_similar:9,sourc:7,source_molecul:7,speci:0,specifi:[0,7,8,12],specifii:0,speed:0,speedup:[0,12],spend:0,sphinx:0,split:0,springer:0,start:[0,6],state:8,statist:0,step:0,store:[7,12],str:[7,8,9,10,12],strategi:[8,9],string:[7,8,12],structur:0,subclass:9,submodul:5,subpackag:5,subsampl:[9,12],subsample_subset_s:9,substanti:0,substitut:0,substrat:0,sulfon:0,sulfonamid:0,suppli:[7,8,9,10],support:[0,2,6],susbtrat:0,svg:0,synthes:0,synthesi:0,t:[0,7],tag:8,take:0,tanimoto:[1,12],target:[0,7],target_mol:7,target_molecul:7,task:[0,3,5,6,12],task_manag:[5,6],taskmanag:9,teardownclass:12,temporari:12,termin:0,test:[0,2,5],test_all_supported_measur:12,test_clustering_fingerprint:12,test_comparetargetmolecul:5,test_descriptor:5,test_descriptor_arbitrary_list_init:12,test_descriptor_arbitrary_numpy_init:12,test_descriptor_empty_init:12,test_descriptor_make_fingerprint:12,test_fingerprint_fold:12,test_get_abcd:12,test_get_molecule_least_similar_to:12,test_get_molecule_most_similar_to:12,test_get_most_dissimilar_pair:12,test_get_most_similar_pair:12,test_mol_mol_similarity_w_morgan_tanimoto:12,test_molecul:5,test_molecule_created_w_attribut:12,test_molecule_created_with_no_attribut:12,test_molecule_draw:12,test_molecule_graph_similar_to_itself_morgan_dic:12,test_molecule_graph_similar_to_itself_morgan_l0:12,test_molecule_graph_similar_to_itself_morgan_tanimoto:12,test_moleculeset:5,test_mordred_descriptor:12,test_multithread:5,test_multithreading_consistency_10_thread:12,test_multithreading_consistency_2_thread:12,test_multithreading_consistency_3_thread:12,test_multithreading_consistency_4_thread:12,test_multithreading_consistency_5_thread:12,test_multithreading_consistency_6_thread:12,test_multithreading_consistency_7_thread:12,test_nonexistent_mordred_descriptor:12,test_pca_transform:12,test_set_molecule_database_fingerprint_from_csv:12,test_set_molecule_database_from_csv:12,test_set_molecule_database_from_excel:12,test_set_molecule_database_from_pdb_dir:12,test_set_molecule_database_from_smarts_fil:12,test_set_molecule_database_from_smi_fil:12,test_set_molecule_database_from_smiles_fil:12,test_set_molecule_database_from_textfil:12,test_set_molecule_database_w_descriptor_property_from_csv:12,test_set_molecule_database_w_descriptor_property_from_excel:12,test_set_molecule_database_w_fingerprint_similarity_from_csv:12,test_set_molecule_database_w_property_from_csv:12,test_set_molecule_database_w_property_from_excel:12,test_set_molecule_database_w_property_from_textfil:12,test_set_molecule_database_w_similarity_from_csv:12,test_set_molecule_from_fil:12,test_set_molecule_from_smil:12,test_similarity_measure_limit:12,test_similaritymeasur:5,test_smart:12,test_smil:12,test_speedup_efficiency_cosin:12,test_speedup_efficiency_tanimoto:12,test_subsample_molecule_database_from_csv:12,test_subsample_molecule_database_from_excel:12,test_subsample_molecule_database_from_pdb_dir:12,test_subsample_molecule_database_from_textfil:12,test_topological_fprint_min_path_lesser_than_atom:12,testcas:12,testcomparetargetmolecul:12,testdescriptor:12,testmolecul:12,testmoleculeset:12,testmultithread:12,testsimilaritymeasur:12,text:[0,12],textfil:12,than:[0,10],theori:0,therebi:0,therefor:8,thi:[0,7,8,9,10],third:10,thread:12,three:0,through:[0,12],thu:0,ti:7,tibshirani:0,time:[0,12],titl:10,tkinter:7,to_key_val_str:10,to_numpi:8,to_rdkit:8,toler:0,too:0,tool:0,top:9,topolog:0,torsion:10,train:0,transform:[0,12],transit:7,tupl:7,tutori:2,twine:0,two:[0,8,12],txt:0,type:[6,9,10,12],typeerror:12,ui:[3,5,8],uintsparseintvec:8,un:[0,7],uniniti:7,uniqu:8,unit:12,unittest:[0,12],unseen:0,unsupervis:12,up:0,upload:0,us:[0,6,7,8,9,10,12],user:[0,8],util:[5,6],v2:0,valu:[0,7,8,9,10,12],valueerror:[6,7,12],variat:0,vector:[7,8,10,12],verif:0,verifi:[0,12],via:9,view:0,virtual:0,visual:[0,9],visualize_dataset:[5,6],visualizedataset:9,vlacho:0,vs:10,ward:0,watson:0,we:0,well:0,when:[0,6,9,12],where:0,which:[0,7,8,9,10],why:0,widm:0,willi:0,window:7,wire:0,without:6,word:7,work:[2,12],x:[7,8,10],xlabel:10,xlabel_fonts:10,xtick:10,xtick_label:10,y:[0,10],yaml:0,yield:0,ylabel:10,ylabel_fonts:10,you:0,your:0},titles:["molSim README","Supported Similarity Metrics","molSim documentation","interfaces package","interfaces.UI package","molSim","molSim package","molSim.chemical_datastructures package","molSim.ops package","molSim.tasks package","molSim.utils package","setup module","tests package"],titleterms:{"function":0,ccbmlib_fingerprint:10,chemical_datastructur:7,cite:0,cluster:8,cluster_data:9,compare_target_molecul:9,conda:0,config_read:3,content:[2,3,4,6,7,8,9,10,12],credit:0,current:0,descriptor:8,document:[0,2],except:6,fingerprint:0,identify_outli:9,implement:0,indic:2,instal:0,interfac:[3,4],licens:0,measure_search:9,method:0,metric:1,modul:[3,4,6,7,8,9,10,11,12],molecul:7,molecule_set:7,molsim:[0,2,5,6,7,8,9,10],molsim_ui_main:4,op:8,output:8,packag:[3,4,6,7,8,9,10,12],pip:0,plotting_script:10,prefer:0,purpos:0,readm:0,run:0,score:0,see_property_variation_with_similar:9,setup:11,similar:[0,1],similarity_measur:8,submodul:[3,4,6,7,8,9,10,12],subpackag:[3,6],support:[1,8],tabl:2,task:9,task_manag:9,test:12,test_comparetargetmolecul:12,test_descriptor:12,test_molecul:12,test_moleculeset:12,test_multithread:12,test_similaritymeasur:12,tutori:0,type:8,ui:4,util:10,visualize_dataset:9,work:0}})