import pygame as pg

# grayPixel: pixel -> pixel
# compute and return a gray pixel with the same intensity
# as the given pixel


def grayPixel(pixel):
    red_intensity = int(pixel[0])
    green_intensity = int(pixel[1])
    blue_intensity = int(pixel[2])
    ave_intensity = (red_intensity + green_intensity + blue_intensity)/3
    return (ave_intensity, ave_intensity, ave_intensity)

# channel: pixel -> channel -> pixel
# return a gray pixel with intensity from given channel of given pixel


def channel(pixel, chan):
    return (pixel[chan], pixel[chan], pixel[chan])


# inverse: pixel -> pixel
# return the color negative of the given pixel
def inverse(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])


# intensify: pixel -> nat255 -> pixel
# brighten each channel of pixel by quantity

def dark(pixel):

    for i in range(0, 3):
        if (pixel[i] > 10):
            pixel[i] -= 10

        else:
            pixel[i] = 0

    return(pixel[0], pixel[1], pixel[2])


def darkIt(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    pixels3d = pg.surfarray.pixels3d(image_surf)

    for x in range(rows):
        for y in range(cols):

            pixels3d[x, y] = dark(pixels3d[x, y])


def bright(pixel):

    for i in range(0, 3):
        if (pixel[i] < 245):
            pixel[i] += 10

        else:
            pixel[i] = 255

    return(pixel[0], pixel[1], pixel[2])


def brightIt(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    pixels3d = pg.surfarray.pixels3d(image_surf)

    for x in range(rows):
        for y in range(cols):

            pixels3d[x, y] = bright(pixels3d[x, y])


def gray(image_surf):

    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    pixels3d = pg.surfarray.pixels3d(image_surf)

    for x in range(rows):
        for y in range(cols):

            pixels3d[x, y] = grayPixel(pixels3d[x, y])


def invert(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x, y] = inverse(pixels3d[x, y])



































