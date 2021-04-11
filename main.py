from image_redactor import Image_redactor
from constants import schema_flot


ir = Image_redactor(schema_flot)
#ir.paint_dots(ir.get_human_dots(100,100))
#ir.show(0)
ir.logic.find_point()