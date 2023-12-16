import os, sys, math
from Bio.PDB import *
import numpy as np



# Define some functions to work with #
def get_peptidic_bond_dihedral(chain, res_id):

    vector_CA1 = chain[res_id]["CA"].get_vector()
    vector_C = chain[res_id]["C"].get_vector()
    vector_N = chain[res_id+1]["N"].get_vector()
    vector_CA2 = chain[res_id+1]["CA"].get_vector()
    peptidic_dihedral = calc_dihedral(vector_CA1, vector_C, vector_N, vector_CA2)

    return math.degrees(peptidic_dihedral)


def get_phi_dihedral(chain, res_id):

    vector_C1 = chain[res_id-1]["C"].get_vector()
    vector_N = chain[res_id]["N"].get_vector()
    vector_CA = chain[res_id]["CA"].get_vector()
    vector_C2 = chain[res_id]["C"].get_vector()
    phi_dihedral = calc_dihedral(vector_C1, vector_N, vector_CA, vector_C2)

    return math.degrees(phi_dihedral)


def get_psi_dihedral(chain, res_id):

    vector_N1 = chain[res_id]["N"].get_vector()
    vector_CA = chain[res_id]["CA"].get_vector()
    vector_C = chain[res_id]["C"].get_vector()
    vector_N2 = chain[res_id+1]["N"].get_vector()
    psi_dihedral = calc_dihedral(vector_N1, vector_CA, vector_C, vector_N2)

    return math.degrees(psi_dihedral)


if __name__ == "__main__":

    # Get the input PDB file as an argument #
    input_pdb = os.path.abspath(sys.argv[1])
    # Create the structure object #
    parser = PDBParser()
    structure = parser.get_structure("input", input_pdb)
    # Get one chain #
    for chain in structure[0].get_chains():
        # Define lists where the dihedrals will be stored #
        pep_list = []
        phi_list = []
        psi_list = []
        # Iterate the residues in that chain #
        for res in chain:
            res_id = int(res.get_id()[1])
            # Calculate dihedrals #
            try:
                pep_dihedral = get_peptidic_bond_dihedral(chain, res_id)
                phi_dihedral = get_phi_dihedral(chain, res_id)
                psi_dihedral = get_psi_dihedral(chain, res_id)
                # Store dihedrals in lists #
                pep_list.append(pep_dihedral)
                phi_list.append(phi_dihedral)
                psi_list.append(psi_dihedral)
            except:
                continue
        # We only analyze one chain, this script is thought for proteins with only one chain #
        break

    # Create the plot #
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')
    plt.plot(phi_list, psi_list, 'x', color='black')
    plt.show()






