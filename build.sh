NAME=$1
THEME=$2
if [ -z "$THEME" ] ; then
  THEME=django
fi
python rst-directive.py \
    --stylesheet=pygments.css \
    --theme-url=ui/${THEME} \
    --traceback \
    ${NAME}.rst > ${NAME}.html
