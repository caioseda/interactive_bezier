# ALL_POINTS = [[(-200,0),(200,0)],[]]
ALL_POINTS = [[]]
def setup():
    size(900,900)
    # applyMatrix(1,0,0,0,50,0)
    ellipseMode(CENTER)
 
def draw():
    global ALL_POINTS
    
    background(255)
    trans = (width/2,height/2)
    translate(*trans)
    
    instrucao()
    
    t = map(mouseY-trans[0],height/2,-height/2,0,1)
    if ALL_POINTS[0]:
        ALL_POINTS = gera_bezier(ALL_POINTS,t)
        draw_lines(ALL_POINTS)
        draw_points(ALL_POINTS)      
        draw_shape(ALL_POINTS,t)
                   
def instrucao():
    if not ALL_POINTS[0]: 
        fill(0)
        textAlign(CENTER, CENTER)
        text("Click to start.",0,0)
        fill(0)
        textAlign(LEFT, CENTER)
        text("Left mouse button: Add point",(-width/2)+30,(-height/2)+20)
        text("Right mouse button: remove point",(-width/2)+30,(-height/2)+30)

def mouseClicked(): 
    global ALL_POINTS
    if mouseButton == LEFT:
        ALL_POINTS[0].append((mouseX - width/2,mouseY - height/2))
    else:
        ALL_POINTS[0].pop()
        ALL_POINTS.pop()
        ALL_POINTS[-1] = []

def draw_points(points):
    for bezier_degree, pontos in enumerate(points):
        for x,y in pontos:
            if bezier_degree==0:
                fill(255,0,0)
                strokeWeight(1)
                p_size=(7,7)
            elif bezier_degree==len(points)-2:
                fill(0,255,0)
                strokeWeight(1)
                p_size=(10,10)
            else:
                fill(127)
                strokeWeight(0)
                p_size=(5,5)
                
            ellipse(x,y,p_size[0],p_size[1])

def draw_lines(points):
    for bezier_degree, pontos in enumerate(points):
        if len(pontos)>=2:
            for i in range(len(pontos)-1):
                p1 = pontos[i]
                p2 = pontos[i+1]
                
                x1, y1 = p1
                x2, y2 = p2
                
                if bezier_degree==0:
                    stroke(0)
                    strokeWeight(2)
                else:
                    stroke(0)
                    strokeWeight(1)
                line(x1, y1, x2, y2)

def draw_shape(points,t):
    print(points[0])
    if len(points[0]) >=2:
        shape_points = []
        for i in range(0,int(t*200)):        
            new_points = gera_bezier(points,i*.005)[-2][0]
            shape_points.append(new_points)
        
        noFill()
        stroke(0,255,0)
        strokeWeight(5)
        beginShape()
        for x,y in shape_points:
            vertex(x,y)
        endShape()

def gera_bezier(points,t):
    for bezier_degree, pontos in enumerate(points):
        if len(pontos)>=2:
            new_points = deriva(pontos, t)
            points[bezier_degree+1] = new_points
        elif len(pontos)==1:
            if points[-1]:
                points.append([])
    return points

def deriva(pontos,t):
    new_points = []
    for i in range(len(pontos)-1):
        p1 = pontos[i]
        p2 = pontos[i+1]
                
        x1, y1 = p1
        x2, y2 = p2
                
        x3 = x1 + t*(x2-x1)
        y3 = y1 + t*(y2-y1)
        
        new_points.append((x3,y3))
    return new_points

    
