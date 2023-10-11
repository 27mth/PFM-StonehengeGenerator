import maya.cmds as cm

'''Let's make some stonehenge together:D'''

#Global Variable
global meshSizeField
global meshNumField
global meshRadField
clickTimeCount=0

#UI setup
def stoneUI():
    global meshSizeField
    global meshNumField
    global meshRadField

    window1='StoneMaker'
    cm.window(t=window1)
    cm.columnLayout( adj=True, h=250, w=250 )
    cm.text( l='How large is the stone?(>0)' )
    meshSizeField=cm.floatField( min=0, value=1 )
    cm.text( l='How many stones?(>3 maybe?)' )
    meshNumField=cm.intField( min=1, max=30, value=3 )
    cm.text( l='How long is the radius?(>1)' )
    meshRadField=cm.floatField( min=1, value=1 )
    cm.text( l='First' )
    cm.button( l='Place Your Locator', c=lctp)
    cm.text( l='Second' )
    cm.button( l='Generate', c=stoneMaker)
    cm.showWindow()

#Locator generator(only one)
def lctp(*arg):
    cm.delete(cm.ls('PlaceMe*'))
    cm.spaceLocator(n='PlaceMe')

#Build the meshes
def stoneMaker(*arg):
    global meshSizeField
    global meshNumField
    global meshRadField
    global clickTimeCount

    meshSize = cm.floatField(meshSizeField, query=True, value=True)
    meshNum = cm.intField(meshNumField, query=True, value=True)
    meshRad = cm.floatField(meshRadField, query=True, value=True)
    clickTimeCount+=1

    gp = cm.group(em=True, n="meshes")


    #Left Stone
    cm.polyCube(h=5*meshSize, w=meshSize, d=2*meshSize, n='stoneL'+str(clickTimeCount))
    cm.move(0, 5*meshSize/2, -meshSize*1.5)
    #Right Stone
    cm.polyCube(h=5*meshSize, w=meshSize, d=2*meshSize, n='stoneR'+str(clickTimeCount))
    cm.move(0, 5*meshSize/2, meshSize*1.5)
    #Top Stone
    cm.polyCube(h=0.5*meshSize, w=1.5*meshSize, d=4*meshSize, n='stoneT'+str(clickTimeCount))
    cm.move(0, 5.25*meshSize, 0)

    #Group them and center pivot
    Group=cm.group( cm.ls('stoneL'+str(clickTimeCount)), cm.ls('stoneR'+str(clickTimeCount)), cm.ls('stoneT'+str(clickTimeCount)), n='stoneGP'+str(clickTimeCount) )
    cm.move(6*meshRad, 0, 0)
    cm.xform(ws=True, a=True, rp=(0, 0, 0))
    cm.makeIdentity(a=True, t=1, r=1, s=1)

    #Calculate user's locater
    cm.matchTransform(cm.ls(sl=True), 'PlaceMe')

    #Duplicate using numbers and make them into a group
    RoD=360/meshNum
    cm.parent(cm.ls(sl=True), gp)
    for i in range(0,meshNum-1):
        cm.duplicate()
        cm.rotate(0, str(RoD)+'deg', 0, r=True)
    