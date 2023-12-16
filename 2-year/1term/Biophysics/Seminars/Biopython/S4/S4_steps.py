from Bio.PDB import *
parser=PDBParser()
structure= parser.get_structure("2dkt", "2dkt.pdb")
model =structure[0]
structure
model
chain=model["A"]
chain
residue=chain[94]#we want to get
residue["CA"]
residue["CA"]
atom_ca=residue["CA"]

#S4 p26 Calculate distances using biopython.PDB
    #Main chain nitrogen of Lysine 132 and carbonil oxigen of histidine 133
residue=chain[132]
residue
Lresidue=chain[132] #Main chain of Lysine 132
Hresidue=chain[133] #Main chain of Histidine 133 --not needed, can skip step
N_132=Lresidue["N"] #Main chain of Nitrogen in Lys 132

O_133=chain[133]["O"] #Carbonile oxide of chain 133

N_132-O_133 #=4.31

#extra


#DIHEDRALS
#prot N to C, for a dihedral we take one of the terms of another residue
#\angle
#- in line(vertex)

#DIHEDRAL for 132
    #phi N->CA

    #C\N-CA\C
    #C-term from prev aa, all from our aa
v1=chain[131]["C"].get_vector()
v2=chain[132]["N"].get_vector()
v3=chain[132]["CA"].get_vector()
v4=chain[132]["C"].get_vector()
phi_dihedral = calc_dihedral(v1, v2, v3, v4)

    #psy CA->C

    #N\CA-C\N
    #all from ours, N-term from next aa
v1=chain[132]["N"].get_vector()
v2=chain[132]["CA"].get_vector()
v3=chain[132]["C"].get_vector()
v4=chain[133]["N"].get_vector()
psi_dihedral = calc_dihedral(v1, v2, v3, v4)


#DIHEDRAL for 133
    #phi
v1=chain[132]["C"].get_vector()
v2=chain[133]["N"].get_vector()
v3=chain[133]["CA"].get_vector()
v4=chain[133]["C"].get_vector()
phi_dihedral = calc_dihedral(v1, v2, v3, v4)
    #psy
v1=chain[133]["N"].get_vector()
v2=chain[133]["CA"].get_vector()
v3=chain[133]["C"].get_vector()
v4=chain[134]["N"].get_vector()
psi_dihedral = calc_dihedral(v1, v2, v3, v4)

#we can iterate on n(132) to get all phi and psy values, we can use them for ramachandran
