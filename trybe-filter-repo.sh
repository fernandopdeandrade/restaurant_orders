### GIT FILTER-REPO ###

## NÃO EXECUTE ESSE SCRIPT DIRETAMENTE
## Esse script foi feito para uso do
## script 'trybe-publisher' fornecido 
## pela Trybe. 

[[ $# == 1 ]] && \
[[ $1 == "trybe-security-parameter" ]] && \
git filter-repo \
    --path .trybe \
    --path .github \
    --path trybe.yml \
    --path trybe-filter-repo.sh \
    --path tests/conftest.py \
    --path tests/ingredients.py \
    --path tests/test_app.py \
    --path tests/test_inventory_control.py \
    --path tests/test_menu_builder.py \
    --path tests/test_menu_data.py \
    --path tests/ingredient/conftest.py \
    --path tests/ingredient/mocks.py \
    --path tests/dish/conftest.py \
    --path tests/dish/mocks.py \
    --path tests/mocks \
    --path README.md \
    --invert-paths --force
