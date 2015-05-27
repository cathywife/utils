#!/usr/bin/python


can_handle = False 


try:
    raise Exception("raise a exception !")
except Exception, e:
  if not can_handle:
      raise
  print str(e) 

