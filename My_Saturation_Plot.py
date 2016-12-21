__author__ = 'kaihami'

import itertools
import warnings
import os
import shlex

class FileOrSequence( object ):
   """ The construcutor takes one argument, which may either be a string,
   which is interpreted as a file name (possibly with path), or a
   connection, by which we mean a text file opened for reading, or
   any other object that can provide an iterator over strings
   (lines of the file).

   The advantage of passing a file name instead of an already opened file
   is that if an iterator is requested several times, the file will be
   re-opened each time. If the file is already open, its lines can be read
   only once, and then, the iterator stays exhausted.

   Furthermore, if a file name is passed that end in ".gz" or ".gzip"
   (case insensitive), it is transparently gunzipped.
   """

   def __init__( self, filename_or_sequence ):
      self.fos = filename_or_sequence
      self.line_no = None

   def __iter__( self ):
      self.line_no = 1
      if isinstance( self.fos, str ):
         if self.fos.lower().endswith( ( ".gz" , ".gzip" ) ):
            lines = gzip.open( self.fos )
         else:
            lines = open( self.fos )
      else:
         lines = self.fos
      for line in lines:
         yield line
         self.line_no += 1
      if isinstance( self.fos, str ):
         lines.close()
      self.line_no = None

   def __repr__( self ):
      if isinstance( self.fos, str ):
         return "<%s object, connected to file name '%s'>" % (
            self.__class__.__name__, self.fos )
      else:
         return "<%s object, connected to %s >" % (
            self.__class__.__name__, repr( self.fos ) )

   def get_line_number_string( self ):
      if self.line_no is None:
         if isinstance( self.fos, str ):
            return "file %s closed" % self.fos
         else:
            return "file closed"
      if isinstance( self.fos, str ):
         return "line %d of file %s" % ( self.line_no, self.fos )
      else:
         return "line %d" % self.line_no

class SAM_Reader(FileOrSequence):
   """A SAM_Reader object is associated with a SAM file that
   contains short read alignments. It can generate an iterator of Alignment
   objects."""

   def __iter__( self ):
      for line in FileOrSequence.__iter__( self ):
         if line.startswith( "@" ):
            # do something with the header line
            continue
         try:
            algnt = SAM_Alignment.from_SAM_line( line )
         except ValueError, e:
            e.args = e.args + ( self.get_line_number_string(), )
            raise
         yield algnt

a = SAM_Reader("/home/kaihami/Desktop/file.txt")
sam_file =

sam_file_path = "/home/kaihami/Desktop/file.txt"
sam_file = open(sam_file_path, 'r').read().split('\n')
for line in sam_file:
    if line == 1:
        print line
    else:
        break