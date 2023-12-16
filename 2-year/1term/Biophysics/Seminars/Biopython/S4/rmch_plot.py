from Bio.PDB import *
parser=PDBParser()
structure= parser.get_structure("2dkt", "/home/jj/Desktop/Bioinformatics/2nd_year/Biophysics/Seminars/Biopython/S4/2dkt.pdb")
model =structure[0]
chain=model["A"]
phi=[]
psy=[]
t=0
#problems when c is <Residue ZN het=H_ZN resseq=191 icode= > , t is 143
for c in chain.get_residues():
    c=str(c)
    c=c.split()
    c=c[3]
    c=int(c[7:])
    if t==0:
        t=c
        continue
        #break#do it for c-1=c and c+1=c+2, we dont want to do it for first
        #t is previous c, as c-1 dont work for first nor last
        #with previous c we can analyze independently of jumps in the sequence
    else:
        v1=chain[t]["C"].get_vector()
        v2=chain[c]["N"].get_vector()
        v3=chain[c]["CA"].get_vector()
        v4=chain[c]["C"].get_vector()
        phi_dieh= calc_dihedral(v1, v2, v3, v4)
        phi.append(phi_dieh)
        v1=chain[t]["N"].get_vector()
        v2=chain[t]["CA"].get_vector()
        v3=chain[t]["C"].get_vector()
        v4=chain[c]["N"].get_vector()
        psy_dieh= calc_dihedral(v1, v2, v3, v4)
        psy.append(psy_dieh)
    t=c
print(phi)