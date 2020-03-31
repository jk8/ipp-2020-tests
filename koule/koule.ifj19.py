def print_line(width):
  line = '+'
  x = 0
  while x < width:
    line = line + '-'
    x = x + 1
  line = line + '+'
  print(line)
  
def pixel_color(lightness):
  if (lightness > 0.900000):
    return '#'
  else:
    if (lightness > 0.700000):
      return '*'
    else:
      if (lightness > 0.500000):
        return '+'
      else:
        if (lightness > 0.300000):
          return '-'
        else:
          if (lightness > 0.100000):
            return '.'
          else:
            return ' '

def abs(val):
  if val < 0:
    return 0 - val
  else:
    return val
  
def yiplus1(d):  
  yi = d
  delta = 1
  while (delta > 0.000100):
    yip1 = (0.500000 * ((d / yi) + yi))
    delta = (yip1 - yi)
    delta = abs(delta)
    yi = yip1
  return yi

def is_in_range(val, min, max):  
  if val > min:
    if val < max:
      return 1
    else:
      pass
  else:
    pass
  return 0

print('ifj-raytracer, vykresli 3 koule')
resx = 70.000000
resy = 60.000000
posx = 0.000000
posy = 0.000000
posz = 0 - 20.000000
spherex = 0.000000
spherey = 0.000000
spherez = 0.000000
sphereradius = 4.000000
lightx = 0 - 5.000000
lighty = 5.000000
lightz = 0 - 11.000000
line = '+'
x = 0.000000
y = 3.000000 

print_line(resx)
 
while (y < resy):
  line = '|'
  x = 0.000000
  while (x < resx):
    tarx = ((1.000000 - ((x * 2.000000) / resx)) * 7.000000)
    tary = ((1.000000 - ((y * 2.000000) / resy)) * 5.000000)
    tarz = 0.000000
    rayx = (tarx - posx)
    rayy = (tary - posy)
    rayz = (tarz - posz)
    n = 0
    z = 9999.000000
    pixel = ' '
    while (n < 3):
      if (n == 0):
        spherex = (0 - 5.000000)
        spherey = (0 - 3.000000)
        spherez = 6.000000
        sphereradius = 3.000000
      else:
        if (n == 1):
          spherex = (0 - 1.000000)
          spherey = 1.000000
          spherez = 10.000000
          sphereradius = 5.000000
        else:
          spherex = 5.000000
          spherey = (0 - 3.000000)
          spherez = 20.000000
          sphereradius = 8.000000

      sphereradius2 = (sphereradius * sphereradius)
      ocx = (posx - spherex)
      ocy = (posy - spherey)
      ocz = (posz - spherez)
      a = (((rayx * rayx) + (rayy * rayy)) + (rayz * rayz))
      b = (2.000000 * (((rayx * ocx) + (rayy * ocy)) + (rayz * ocz)))
      c = ((((ocx * ocx) + (ocy * ocy)) + (ocz * ocz)) - sphereradius2)
      d = ((b * b) - ((4.000000 * a) * c))
      if (d > 0.000000):
        d = yiplus1(d)
        t = (((0.000000 - b) - d) / (2.000000 * a))
        in_range = is_in_range(t, 0, z)
        if in_range:
          z = t
          intersectionx = ((rayx * t) + posx)
          intersectiony = ((rayy * t) + posy)
          intersectionz = ((rayz * t) + posz)
          normalx = ((intersectionx - spherex) / sphereradius)
          normaly = ((intersectiony - spherey) / sphereradius)
          normalz = ((intersectionz - spherez) / sphereradius)
          tolightx = (lightx - intersectionx)
          tolighty = (lighty - intersectiony)
          tolightz = (lightz - intersectionz)
          d = (((tolightx * tolightx) + (tolighty * tolighty)) + (tolightz * tolightz))
          d = yiplus1(d)
          lightness = ((((normalx * tolightx) + (normaly * tolighty)) + (normalz * tolightz)) / d)
          pixel = pixel_color(lightness)
        else:
          pass
      else:
        pass
      n = n + 1

    line = line + pixel
    x = x + 1.000000

  line = line + '|'
  print(line)
  y = y + 1.000000

print_line(resx)

