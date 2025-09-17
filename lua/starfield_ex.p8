pico-8 cartridge // http://www.pico-8.com
version 42
__lua__
--stars, hopefully

FUNCTION _INIT()
 STARS={}
 STAR_COLS={1,2,5,6,7,12}
 WARP_FACTOR=3

 FOR I=1,#STAR_COLS DO
  FOR J=1,10 DO
   LOCAL S={
    X=RND(128),
    Y=RND(128),
    Z=I,
    C=STAR_COLS[I]
   }
   ADD(STARS,S)
  END 
 END
END

FUNCTION _UPDATE60()
 FOR S IN ALL(STARS) DO
  S.Y+=S.Z*WARP_FACTOR/10
  IF S.Y>128 THEN
   S.Y=0
   S.X=RND(128)
  END
 END
END

FUNCTION _DRAW()
 CLS()
 FOR S IN ALL(STARS) DO
  PSET(S.X,S.Y,S.C)
 END
END