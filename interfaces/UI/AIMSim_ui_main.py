"""User Interface and associated methods to access the key functionalities of
AIMSim without having to use the command line.

Raises:
    IOError: When pressing 'open config' it is possible that no suitable
    program will be known to the OS to open .yaml files. Also if no tasks
    are selected, an IOError will be raised.

Author:
    Jackson Burns
"""
from aimsim.tasks.task_manager import TaskManager
from aimsim.ops.descriptor import Descriptor
from aimsim.ops.similarity_measures import SimilarityMeasure

import yaml
import os
import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
import webbrowser
import pkg_resources


import customtkinter as ctk


class AIMSimUiApp(ctk.CTk):
    """User interface to access key functionalities of AIMSim."""

    def __init__(self, master=None):
        """Constructor for AIMSim.

        Args:
            master (tk, optional): tk window. Defaults to None.
        """
        # build ui
        self.window = ctk.CTk() if master is None else ctk.CTkToplevel(master)
        self.window.title("AIMSim")

        # add the logo
        # resource_path = pkg_resources.resource_filename(
        #     __name__,
        #     "AIMSim-logo.png",
        # )
        # self.window.iconphoto(False, tk.PhotoImage(file=resource_path))

        # setup attributes to hold files, variables, etc.
        self.databaseFile = tk.StringVar(self.window)
        self.targetMolecule = tk.StringVar(self.window)
        self.similarityMeasure = tk.StringVar(self.window)
        self.molecularDescriptor = tk.StringVar(self.window)

        # title
        self.titleLabel = ctk.CTkLabel(self.window)
        self.titleLabel.configure(
            font="TkDefaultFont 14 bold", text="AI Molecular Similarity")
        self.titleLabel.place(anchor="center", relx="0.5",
                              rely="0.05", x="0", y="0")
        self.mainframe = ctk.CTkFrame(self.window)

        # checkbox for verbosity
        self.verboseCheckbutton = ctk.CTkCheckBox(
            self.mainframe,
            cursor="arrow",
            offvalue="False",
            onvalue="True",
            state=tk.NORMAL,
            text="Verbose",
        )
        self.verboseCheckbutton.place(
            anchor="center", relx="0.1", rely="0.95", x="0", y="0"
        )

        # text entry field for molecule database
        self.databaseFileEntry = ctk.CTkEntry(
            self.mainframe, textvariable=self.databaseFile
        )
        _text_ = """smiles_responses.txt"""
        self.databaseFileEntry.delete("0", "end")
        self.databaseFileEntry.insert("0", _text_)
        self.databaseFileEntry.place(
            anchor="center", relx="0.5", rely="0.08", x="0", y="0"
        )

        # database file browser button
        self.browseButton = ctk.CTkButton(self.mainframe)
        self.browseButton.configure(text="Browse...")
        self.browseButton.place(
            anchor="center",
            relx="0.85",
            rely="0.08",
            x="0",
            y="0",
        )
        self.browseButton.configure(command=self.browseCallback)

        # label for database entry line
        self.databaseFileLabel = ctk.CTkLabel(self.mainframe)
        self.databaseFileLabel.configure(text="Database File:")
        self.databaseFileLabel.place(
            anchor="center", relx="0.5", rely="0.02", x="0", y="0"
        )

        # entry field for target molecule
        self.targetMoleculeEntry = ctk.CTkEntry(
            self.mainframe, textvariable=self.targetMolecule
        )
        _text_ = """CO"""
        self.targetMoleculeEntry.delete("0", "end")
        self.targetMoleculeEntry.insert("0", _text_)
        self.targetMoleculeEntry.place(
            anchor="center", relx="0.5", rely="0.28", x="0", y="0"
        )

        # label for target molecule
        self.targetMoleculeLabel = ctk.CTkLabel(self.mainframe)
        self.targetMoleculeLabel.configure(text="Target Molecule:")
        self.targetMoleculeLabel.place(
            anchor="center", relx="0.5", rely="0.22", x="0", y="0"
        )

        # checkbox for database similarity plots
        self.similarityPlotsCheckbutton = ctk.CTkCheckBox(self.mainframe)
        self.similarityPlotsCheckbutton.configure(text="Similarity Plots")
        self.similarityPlotsCheckbutton.place(
            anchor="center", relx="0.3", rely="0.15", x="0", y="0"
        )

        # checkbox for property similarity plot
        self.propertySimilarityCheckbutton = ctk.CTkCheckBox(self.mainframe)
        self.propertySimilarityCheckbutton.configure(
            text="Property Similarity Plot")
        self.propertySimilarityCheckbutton.place(
            anchor="center", relx="0.7", rely="0.15", x="0", y="0"
        )

        # Similarity plot for target molecule
        self.similarityPlotCheckbutton = ctk.CTkCheckBox(self.mainframe)
        self.similarityPlotCheckbutton.configure(text="Similarity Plot")
        self.similarityPlotCheckbutton.place(
            anchor="center", relx="0.5", rely="0.35", x="0", y="0"
        )

        # dropdown for descriptors
        self.similarityMeasureCombobox = ctk.CTkComboBox(
            self.mainframe, variable=self.similarityMeasure, state="readonly"
        )
        self.similarityMeasureCombobox.configure(
            takefocus=False, values=SimilarityMeasure.get_supported_metrics()
        )
        self.similarityMeasureCombobox.set(0)
        self.similarityMeasureCombobox.place(
            anchor="center", relx="0.5", rely="0.46", x="0", y="0"
        )

        # label for similarity metric
        self.similarityMeasureLabel = ctk.CTkLabel(self.mainframe)
        self.similarityMeasureLabel.configure(text="Similarity Measure:")
        self.similarityMeasureLabel.place(
            anchor="center", relx="0.5", rely="0.4", x="0", y="0"
        )

        # label for descriptor dropdown
        self.molecularDescriptorLabel = ctk.CTkLabel(self.mainframe)
        self.molecularDescriptorLabel.configure(text="Molecular Descriptor:")
        self.molecularDescriptorLabel.place(
            anchor="center", relx="0.5", rely="0.54", x="0", y="0"
        )

        # do not allow changes
        self.molecularDescriptorCombobox = ctk.CTkComboBox(
            self.mainframe, variable=self.molecularDescriptor, state="readonly"
        )
        self.molecularDescriptorCombobox.configure(
            cursor="arrow",
            takefocus=False,
            values=Descriptor.get_supported_fprints(),
        )

        # define the callback for the descriptor
        def updateCompatibleMetricsListener(event):
            """Show only compatible metrics, given a descriptor."""
            self.similarityMeasureCombobox[
                "values"
            ] = SimilarityMeasure.get_compatible_metrics().get(
                self.molecularDescriptor.get(), "Error"
            )
            self.similarityMeasureCombobox.current(0)
            return

        # bind this listener to the combobox
        self.molecularDescriptorCombobox.bind(
            "<<ComboboxSelected>>", updateCompatibleMetricsListener
        )
        self.molecularDescriptorCombobox.place(
            anchor="center", relx="0.5", rely="0.60", x="0", y="0"
        )
        self.molecularDescriptorCombobox.set(0)

        # button to run AIMSim
        self.runButton = ctk.CTkButton(self.mainframe)
        self.runButton.configure(text="Run")
        self.runButton.place(anchor="center", relx="0.5",
                             rely="0.75", x="0", y="0")
        self.runButton.configure(command=self.runCallback)

        # uses default editor to open underlying config file button
        self.openConfigButton = ctk.CTkButton(self.mainframe)
        self.openConfigButton.configure(text="Open Config")
        self.openConfigButton.place(
            anchor="center", relx="0.5", rely="0.85", x="0", y="0"
        )
        self.openConfigButton.configure(command=self.openConfigCallback)

        # checkbox to show all descriptors in AIMSim
        self.showAllDescriptorsButton = ctk.CTkCheckBox(
            self.mainframe,
            cursor="arrow",
            offvalue="False",
            onvalue="True",
            command=self.showAllDescriptorsCallback,
        )
        self.showAllDescriptorsButton.configure(
            state="normal", text="Show experimental descriptors"
        )
        self.showAllDescriptorsButton.place(
            anchor="center", relx="0.5", rely="0.67", x="0", y="0"
        )

        # multiprocessing checkbox
        self.multiprocessingCheckbutton = ctk.CTkCheckBox(
            self.mainframe,
            cursor="arrow",
            offvalue="False",
            onvalue="True"
        )
        self.multiprocessingCheckbutton.configure(
            state=tk.NORMAL, text="Enable Multiple Workers"
        )
        self.multiprocessingCheckbutton.place(
            anchor="center", relx="0.78", rely="0.95", x="0", y="0"
        )

        # checkbox for outlier checking
        self.identifyOutliersCheckbutton = ctk.CTkCheckBox(
            self.mainframe,
            cursor="arrow",
            offvalue="False",
            onvalue="True",
        )
        self.identifyOutliersCheckbutton.configure(
            state=tk.NORMAL, text="Outlier Check")
        self.identifyOutliersCheckbutton.place(
            anchor="center", relx="0.4", rely="0.95", x="0", y="0"
        )

        # dimensions of window
        self.mainframe.configure(height="400", width="400")
        self.mainframe.place(anchor="nw", relheight="0.9",
                             rely="0.1", x="0", y="0")
        self.window.configure(
            cursor="arrow", height="400", relief="flat", takefocus=False
        )
        self.window.configure(width="400")

        # Main widget
        self.mainwindow = self.window

    def browseCallback(self):
        """launch a file dialog and set the databse field"""
        out = filedialog.askopenfilename(
            initialdir=".",
            title="Select Molecule Database File",
            filetypes=[
                ('SMILES', '.smi .txt .SMILES'),
                ('Protein Data Bank', '.pdb'),
                ('Comma-Separated Values', '.csv .tsv'),
                ('Excel Workbook', '.xlsx'),
            ],
        )
        if out:
            self.databaseFile.set(out)
        return

    def showAllDescriptorsCallback(self):
        """update the descriptors dropdown to show descriptors."""
        if "selected" in self.showAllDescriptorsButton.state():
            self.molecularDescriptorCombobox[
                "values"
            ] = Descriptor.get_all_supported_descriptors()
        else:
            self.molecularDescriptorCombobox[
                "values"
            ] = values = Descriptor.get_supported_fprints()
        return

    def openConfigCallback(self):
        """
        Open the config file being used by the UI to allow the user to edit it.

        """
        webbrowser.open("AIMSim-ui-config.yaml")

    def runCallback(self):
        """Retrieves user input, writes to a .yaml configuration file, and calls AIMSim on that input.

        Raises:
            IOError: When opening the automatically generated config file from the UI, there is a chance
            that the OS will not know which program to use, raising the error.
        """
        tasks_dict = {}

        inner_dict = {}
        if "selected" in self.similarityPlotsCheckbutton.state():
            inner_dict["similarity_plot_settings"] = {
                "plot_color": "green",
                "plot_title": "Molecule Database Similarity Distribution",
            }
            inner_dict["heatmap_plot_settings"] = {
                "annotate": False,
                "plot_title": "Molecule Database Pairwise Similarities",
                "cmap": "viridis",
            }
        if len(inner_dict) > 0:
            tasks_dict["visualize_dataset"] = inner_dict
        if "selected" in self.identifyOutliersCheckbutton.state():
            tasks_dict["identify_outliers"] = {"output": "terminal"}
        if "selected" in self.similarityPlotCheckbutton.state():
            tasks_dict["compare_target_molecule"] = {
                "target_molecule_smiles": self.targetMolecule.get(),
                "similarity_plot_settings": {
                    "plot_color": "orange",
                    "plot_title": "Molecule Database Compared to Target Molecule",
                },
                "identify_closest_furthest": {"out_file_path": "AIMSim-ui_output.txt"},
            }
        if "selected" in self.propertySimilarityCheckbutton.state():
            tasks_dict["see_property_variation_w_similarity"] = {
                "property_file": self.databaseFile.get(),
                "most_dissimilar": True,
                "similarity_plot_settings": {"plot_color": "red"},
            }

        verboseChecked = "selected" in self.verboseCheckbutton.state()
        if "selected" in self.multiprocessingCheckbutton.state():
            n_workers = 'auto'
        else:
            n_workers = 1

        _, file_extension = os.path.splitext(self.databaseFile.get())
        if file_extension == ".txt":
            molecule_database_source_type = "text"
        elif file_extension == "":
            molecule_database_source_type = "folder"
        elif file_extension == ".xlsx":
            molecule_database_source_type = "excel"
        else:
            molecule_database_source_type = file_extension.replace(".", "")

        yamlOut = {
            "is_verbose": verboseChecked,
            "n_workers": n_workers,
            "molecule_database": self.databaseFile.get(),
            "molecule_database_source_type": "text",
            "similarity_measure": self.similarityMeasure.get(),
            "fingerprint_type": self.molecularDescriptor.get(),
            "tasks": tasks_dict,
        }

        with open("AIMSim-ui-config.yaml", "w") as outfile:
            yaml.dump(yamlOut, outfile, default_flow_style=False)

        configs = yaml.load(open("AIMSim-ui-config.yaml",
                            "r"), Loader=yaml.FullLoader)

        tasks = configs.pop("tasks")
        if not tasks:
            messagebox.showerror(
                "Unexpected error!",
                "No tasks were selected.",
            )
            return

        try:
            task_manager = TaskManager(tasks=tasks)
            task_manager(molecule_set_configs=configs)
        except Exception as e:
            messagebox.showerror(
                "Unexpected error!",
                e,
            )
            return

    def run(self):
        """Start the UI."""
        self.mainwindow.mainloop()


def main():
    """Start the app."""
    app = AIMSimUiApp()
    app.run()


if __name__ == "__main__":
    app = AIMSimUiApp()
    app.run()
