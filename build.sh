NAME=$1
THEME=$2
PDF=$3
if [ -z "$THEME" ] ; then
  THEME=django
fi
python rst-directive.py \
    --stylesheet=pygments.css \
    --theme-url=ui/${THEME} \
    --traceback \
    ${NAME}.rst > ${NAME}.html


if [ ! -z "$PDF" ] ; then
    sed -e 's/.. sourcecode.*/::/g'  $NAME.rst |perl -e 'while(<>) { if ( m/^.. graph.?::(.*)/) { print ".. image::$1\n\n"; $off = 1; } elsif (m/^\S.*/) { $off = 0; print $_;} elsif(!$off) {print "$_"; };}'  > $NAME.rst.standard 
    rst2pdf $NAME.rst.standard -o $NAME.pdf -s a5-landscape.style
fi



