# README
## 1. Prepare Code Space
- Go to Exstensions & Install Python + Jupyter
- Create gitignore
```bash
echo -e ".venv\n.env" > .gitignore
```
- Create Virtual Enviroment and Activate
```bash
python -m venv .venv
source .venv/bin/activate
```
- Install Python libraries to work with Jupyter, pandas, and matplotlib
```bash
python -m pip install ipykernel nbformat pandas seaborn
```
- Create Work Folders
```bash
mkdir notebooks src app docs
mkdir -p data/{raw,baking,final}
```
- Edit an Archive
```bash
touch mytext.txt
nano mytxt
```
