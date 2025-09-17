pico-8 cartridge // http://www.pico-8.com
version 42
__lua__
--stars, hopefully

function _init()
 stars={}
 star_cols={1,2,5,6,7,12}
 warp_factor=3

 for i=1,#star_cols do
  for j=1,10 do
   local s={
    x=rnd(128),
    y=rnd(128),
    z=i,
    c=star_cols[i]
   }
   add(stars,s)
  end 
 end
end

function _update60()
 for s in all(stars) do
  s.y+=s.z*warp_factor/10
  if s.y>128 then
   s.y=0
   s.x=rnd(128)
  end
 end
end

function _draw()
 cls()
 for s in all(stars) do
  pset(s.x,s.y,s.c)
 end
end