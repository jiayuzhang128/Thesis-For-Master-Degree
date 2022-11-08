from skimage import io

grayscale = io.imread("./RGB1.png", as_gray=True)
io.imsave("./Gray1.png", grayscale)
