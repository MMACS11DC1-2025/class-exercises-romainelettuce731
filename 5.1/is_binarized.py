def is_light(pixel):
    if int(pixel[0] + pixel[1] + pixel[2])/3 > 128:
        return True
    else:
        return False