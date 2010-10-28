NAME=$1
THEME=django
#THEME=default
python rst-directive.py \
    --stylesheet=pygments.css \
    --theme-url=ui/${THEME} \
    --traceback \
    ${NAME}.rst > ${NAME}.html
