from image_redactor import Image_redactor
from constants import schema_flot


ir = Image_redactor(schema_flot)

#рисовать на карте чела
#ir.paint_dots(ir.get_human_dots(100,100))
#ir.show(0)

#point
#ir.logic.find_point()
imgname = "index.jpeg"
ir.find_people(imgname)