#!/bin/bash
FILES=t*-template
for f in $FILES
do
  mv $f ${f/t/gs-}
done
