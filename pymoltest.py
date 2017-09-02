#test

import pymol
from pymol import cmd
pymol.finish_launching(['pymol','-qc'])
cmd.load('1atp.pdb')
cmd.load('1atp2.pdb')
cmd.load('1atp3.pdb')
cmd.spectrum('b', 'blue_white_red','1atp', 0, 100)
cmd.spectrum('b', 'yellow_cyan_blue','1atp2', 0, 100)
cmd.spectrum('b', 'green_magenta','1atp3', 0, 100)
cmd.save('somecolors.pse')
pymol.finish_launching()
