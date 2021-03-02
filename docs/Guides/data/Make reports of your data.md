Tools are provided to generate test or analysis reports, with a custom template. These are generated with the `jupyter nbconvert` using the preprocessor and tools in the `notebooks` and `template` folder. To generate a report, follow the steps:

1. Tag the cells in your notebook. You can use the [Jupyter Lab Celltags](https://github.com/jupyterlab/jupyterlab-celltags) extension. Don't tag the cells you want to hide, and tag the ones you want to show with `show_only_output`. This can be changed and add more tags, but we keep it this way for simplicity

2. Go to the notebooks folder:

```
cd notebooks
```

3. Type the command:

```
jupyter nbconvert --config sc_nbconvert_config.py notebook.ipynb --sc_Preprocessor.expression="show_only_output" --to html --TemplateExporter.template_file=./templates/full_sc --output-dir=../reports --output=OUTPUT_NAME
```

Where:

- `sc_nbconvert_config.py` is the config
- `notebook.ipynb` is the notebook you want
- `"show_only_output"` is a boolean expression that is evaluated for each of the cells. If true, the cell is shown
- `./templates/full_sc` is the default template we have created
- `../reports` is the directory where we will put the `html` report
- `OUTPUT_NAME` is the name for the export

This generates an html export containing only the mkdown or code cell outputs, without any code. Examples can be found in [the source code repository](https://github.com/fablabbcn/smartcitizen-iscape-data/tree/master/data/reports).

!!! info "Don't like the template?"
    You can modify these templates in the [templates folder](https://github.com/fablabbcn/smartcitizen-iscape-data/tree/master/notebooks/templates)

And here is the result!

![](https://i.imgur.com/XNBnRUr.png)