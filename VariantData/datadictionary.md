## Data Dictionary

| **Column Name** | **Description** |
| --- | --- |
| usa\_or\_hhsregion | Specifies the geographic area for the estimate; either national ("USA"), or HHS regions 1 – 10. |
| week\_ending | The date of the last day (Saturday) of the week (or 2-week period) for which an estimate is made |
| variant | The name of the variant that the estimate is for. (Note that some variants are aggregates of all that variant's subvariants.) |
| share | The proportion of the variant |
| share\_hi | The upper bound of the 95% confidence interval for the estimated variant share (prediction intervals for smoothed estimates). |
| share\_lo | The lower bound of the 95% confidence interval for the estimated variant share (prediction intervals for smoothed estimates). |
| nchs\_or\_count\_flag | True if weighted estimate is based on fewer than 10 sequences or any of the following items is identified as unreliable by NCHS standards: degrees of freedom, effective sample size, denominator count, absolute confidence interval width, or relative confidence interval width ([https://www.cdc.gov/nchs/data/series/sr\_02/sr02\_175.pdf](https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf)) |
| modeltype | Estimate is based on weighted data ("weighted') or Nowcasted data ("smoothed") |
| time\_interval | Whether data is base on one week interval ("weekly") or two week intervals ("biweekly") |
| published\_date | Date that this set was published to COVID Data Tracker |
