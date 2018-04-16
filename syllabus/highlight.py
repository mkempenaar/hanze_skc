from pymol import cmd

def highlight(sele):
    cmd.show('spheres', sele)
    cmd.color('yellow', sele)

cmd.extend("highlight", highlight)
