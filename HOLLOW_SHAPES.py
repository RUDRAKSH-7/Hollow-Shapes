from pyglet import shapes

class shallow:
    def rect(x_cor,y_cor,width_,height_,scale : int,color_of_main_rect : list,shallow_color = [0,0,0]):
        rect_ = shapes.Rectangle(x_cor,y_cor,width=width_,height=height_,color=color_of_main_rect)
        _rect_ = shapes.Rectangle(x_cor+(scale//2),y_cor+(scale//2),width=width_-scale,height = height_-scale,color=shallow_color)
        rect_.draw() ; _rect_.draw()