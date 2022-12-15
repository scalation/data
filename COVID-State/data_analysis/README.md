# Paper details

## Datasets
The datasets used in the paper and scripts used to generate the datasets are explained below
- `data/cdc_YYYY-MM-DD-HH-MM-SS.csv` - contains the CDC data. This dataset is built using [data/scripts/create_cdc_data.py](./data/scripts/create_cdc_data.py). Use the following command to run the script `cd data/scripts && python create_cdc_data.py`
- `data/jhu_YYY-MM-DD-HH-MM-SS.csv` - contains the JHU data. This dataset is built using [data/scripts/create_jhu_data.py](./data/scripts/create_jhu_data.py). Use the following command to run the script `cd data/scripts && python create_jhu_data.py`
- `data/jhu_with_cdc_start.cdv` - Contains the JHU data but the value of the total deaths for the start is taken from CDC. This dataset is built using [data/scripts/create_jhu_with_cdc_start.py](./data/scripts/create_jhu_with_cdc_start.py). Use the following command to run the script `cd data/scripts && python data/scripts/create_jhu_with_cdc_start.py`

## Interactive plot
The interactive plot to visualize the discrepancies in the CDC and JHU data is built using [Dash](https://plotly.com/dash/) and be started using `python interactive_plot.py`. This would start a server at `http://127.0.0.1:8050/`.

## Reproducing tables
**Table 1**. Run `example.ipynb` and the cell 3 gives the desired output.

**Table 2**.
- In `interactive_plot.py` make sure the line 121 is uncommented i.e. `print(state, diff['abs'].max().item())`.
- After this run `python interactive_plot.py` and once the data is rendered on screen, the desired output would be outputted in termial.
- Now you can copy this data to Excel and sort by the difference to get the top-6 states with the maximum difference.

### Reproducing figures
**Figure 1**
- In `interactive_plot.py` make sure line 11 is uncommented and line 12 is commented i.e. 
    ```python
    jhu = pd.read_csv('./data/jhu_2022-11-18-05-14-54.csv')
    # jhu = pd.read_csv('./data/jhu_with_cdc_start.csv')
    ```
- After this run `python interactive_plot.py` and you can see the plots for the state of GA with moving average 1, 3, and 7.

**Figure 2**
- In `interactive_plot.py` make sure line 11 is commented and line 12 is uncommented i.e. 
    ```python
    # jhu = pd.read_csv('./data/jhu_2022-11-18-05-14-54.csv')
    jhu = pd.read_csv('./data/jhu_with_cdc_start.csv')
    ```
- After this run `python interactive_plot.py` and you can see the plots for the state of GA with moving average 1, 3, and 7.

**Figure 3**
- First reproduce the results for **Table 2** as shown in the previous section
- Then run `python interactive_plot.py` and select running aaverage 1 and get the plots for the top-6 states.

## Embeddings
[https://projector.tensorflow.org/](https://projector.tensorflow.org/) is used to visualize the embeddings. In this tool, there is no option to set the random seed so the results would vary for different runs. The input embbeddings are available in `embeddings/embeddings.tsv` and the corresponding metadata i.e. the name of the state for each embedding is listed in `embeddings/metadata.tsv`.