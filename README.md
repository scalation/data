# data

Please visit this GitHub[https://github.com/mh2t/covid] for more information.  
ScalaTion Dataset Collection

This repository contains a collection of datasets that are used in ScalaTion. The datasets are organized under 5 sub categories. They are

- analytics
- graphanalytics
- linalgebra
- relalgebra
- tableau

Datasets can be downloaded via the `.download.sh` script in the main scalation data directory. See below for usage.

## Installation
```sh
# If scalation is not installed
$ git clone https://github.com/scalation/scalation.git

# Go to the scalation data directory
$ cd scalation/data

# Execute the download script with no arguments to download all datasets
$ ./download.sh

# If you would like only download a single category, then specify it as an argument
$ ./download.sh linalgebra
```


## Regression Datasets
|Name|#rows|#attrs|Size|Description|Path|
|----|------|-----|---------|-----|----|
|auto-mpg|392|8|0.02MB|Auto-MPG Dataset from UCI|analytics/regression/auto_mpg.csv|
|airfoil|1503|5|0.06MB|Airfoil Self Noise Dataset from UCI(NASA)|analytics/regression/airfoil/airfoil_self_noise.csv|
|concrete_compressive|1030|9|0.06MB|Concrete Compressive Strength Dataset from UCI|analytics/regression/concrete_compressive/Concrete_Data.csv|
|ccpp|9568|4|0.29MB|Combined Cycle Power Plant Dataset from UCI|analytics/regression/ccpp/Folds5x2_pp.csv|
|concrete_slump_1|103|10|0.004MB|Concrete Slump Dataset from UCI (target: SLUMP)|analytics/regression/concrete_slump/slump_test.csv|
|concrete_slump_2|103|10|0.004MB|Concrete Slump Dataset from UCI (target: FLOW)|analytics/regression/concrete_slump/slump_test.csv|
|concrete_slump_3|103|10|0.004MB|Concrete Slump Dataset from UCI (target: Compressive Strength)|analytics/regression/concrete_slump/slump_test.csv|
|nist_gauss_1|250|1|0.005MB|NIST Gauss1 dataset. The data are two well-separated Gaussians on a decaying exponential baseline plus normally distributed zero-mean noise with variance = 6.25.|analytics/regression/nist_gauss_1.csv|
|prostate|97|8|0.01MB|R Prostate Cancer dataset|analytics/regression/prostate.csv|
|kin8nm|8192|8|0.66MB|kin8nm dataset from OpenML (https://www.openml.org/d/189)|analytics/regression/dataset_2175_kin8nm.csv|
|computer_activity_1|8192|21|0.69MB|Torgo Computer Activity Dataset|analytics/regression/computer_activity/cpu_act.data|
|computer_activity_2|8192|12|0.43MB|Torgo Computer Activity Dataset - Small version|analytics/regression/computer_activity/cpu_small.data|
|wisconsin_breast|194|32|0.04MB|Wisconsin Breast Cancer Dataset|analytics/regression/wisconsin_breast_cancer/r_wpbc.data|
|auto_price|159|15|0.01MB|Torgo Auto Price Dataset|analytics/regression/auto_price/price.data|
|gym_crowdedness|62184|10|3.29MB|Kaggle Campus Gym Crowdedness Dataset|analytics/regression/gym_crowdedness.csv|
|forest_fire|517|12|0.02MB|UCI Forest Fire Dataset|analytics/regression/forest_fire/forestfires.csv|
|housing|506|13|0.04MB|Boston Housing Dataset|analytics/regression/housing/housing_fixed.csv|
|istanbul_stock|536|9|0.06MB|UCI Istanbul Stock Exchange Dataset|analytics/regression/data_akbilgic.csv|
|tecator_moisture|240|100|0.18MB|OPENML Tecator Dataset(target: Moisture)|analytics/regression/tecator/tecator_moisture.csv|
|tecator_fat|240|100|0.18MB|OPENML Tecator Dataset(target: Fat)|analytics/regression/tecator/tecator_fat.csv|
|tecator_protein|240|100|0.18MB|OPENML Tecator Dataset(target: Protein)|analytics/regression/tecator/tecator_protein.csv|
|bike_sharing_total_hour|17379|16|1.09MB|UCI Bike Sharing Dataset| Hourly Data Total Count|analytics/regression/bike-sharing/hour.csv|
|bike_sharing_total_day|731|15|0.05MB|UCI Bike Sharing Dataset| Daily Data Total Count|analytics/regression/bike-sharing/day.csv|
|bng_breast|116640|9|6.32MB|OPENML BNG Breast Tumor Dataset|analytics/regression/BNG_breastTumor.csv|
|visualizing_soil|8641|4|0.20MB|OPENML Visualizing Soil Dataset|analytics/regression/visualizing_soil.csv|
|bank8fm|8192|8|0.59MB|OPENML Customer Bank Selection Dataset|analytics/regression/bank8fm.csv|
|abalone|4177|8|0.18MB|Torgo Abalone Dataset|analytics/regression/abalone/abalone.data|
|electricity_prices|37682|16|2.77MB|OPENML ICON Electricity Challenge Dataset|analytics/regression/electricity_prices/electricity_prices_nomissing.csv|
|casp|45730|9|3.37MB|UCI Protein Tertiary Structure DataSet |analytics/regression/CASP.csv|
|appliance_energy|19735|28|4.04MB|UCI Appliance Energy DataSet |analytics/regression/appliance_energy/energy_data_clean.csv|
|crime_norm|1993|100|0.90MB|UCI Communities Crime(target: ViolentPerPop) DataSet |analytics/regression/communities/communities.csv|
|parkinson_1|5875|18|0.78MB|UCI Parkinson Telemonitoring Dataset(target: total)|analytics/regression/parkinson/parkinsons_motor_updrs.csv|
|parkinson_2|5875|18|0.78MB|UCI Parkinson Telemonitoring Dataset(target: motor)|analytics/regression/parkinson/parkinsons_total_updrs.csv|
|servo|167|4|0.003MB|UCI Servo Dataset|analytics/regression/servo/servo.data.txt|
|student_1|395|29|0.04MB|UCI Student Performance Dataset(target: mat)|analytics/regression/student/student-mat.csv|
|student_2|649|29|0.06MB|UCI Student Performance Dataset(target: por)|analytics/regression/student/student-por.csv|
|yacht|308|6|0.01MB|UCI Yacht Hydodynamics Dataset|analytics/regression/yacht_hydrodynamics.data|
|fb_metric_1|496|15|0.03MB|UCI Facebook Metric Dataset(target: total)|analytics/regression/fb/dataset_total.csv|
|fb_metric_2|496|15|0.03MB|UCI Facebook Metric Dataset(target: like)|analytics/regression/fb/dataset_like.csv|
|fb_metric_3|496|15|0.03MB|UCI Facebook Metric Dataset(target: comment)|analytics/regression/fb/dataset_comment.csv|
|fb_metric_4|496|15|0.03MB|UCI Facebook Metric Dataset(target: share)|analytics/regression/fb/dataset_share.csv|
|cars|1447|13|0.11MB|Applied Predictive Modeling Cars Dataset(all)|analytics/regression/cars/cars_all.csv|
|chick_weight|578|2|0.004MB|R Caret Package Chick Weight Dataset|analytics/regression/chick_weight.csv|
|life_cycle_savings|50|4|0.001MB|R Caret Package Life Cycle Savings Dataset|analytics/regression/life_cycle_savings.csv|
|hi|22272|11|1.05MB|R Health Insurance Housewives Dataset|analytics/regression/HI.csv|
|body_fat|252|17|0.02MB|Bilkent Body Fat Dataset|analytics/regression/body_fat.csv|
|fried|40768|10|2.55MB|Bilkent Fried Dataset|analytics/regression/fried.csv|
|plastic|1650|2|0.02MB|Bilkent Plastic Dataset|analytics/regression/plastic.csv|
|quake|2178|3|0.04MB|Bilkent Quake Dataset|analytics/regression/quake.csv|
|weather_1|1609|9|0.08MB|Bilkent Weather Ankara Dataset|analytics/regression/WA.dat|
|weather_2|1461|9|0.07MB|Bilkent Weather Izmir Dataset|analytics/regression/WI.dat|
|treasury|1049|15|0.09MB|Bilkent Treasury Dataset|analytics/regression/TR.dat|
|pwlinear|177147|10|5.58MB|OPENML PWLinear Dataset|analytics/regression/BNG_pwLinear.csv|
|puma32h|8192|32|2.40MB|Torgo Puma32H Dataset|analytics/regression/puma32H.csv|
|puma8nh|8192|8|0.66MB|Torgo Puma8NH Dataset|analytics/regression/puma8NH.csv|
|2dplanes|40768|10|1.25MB|Torgo 2dplanes Dataset|analytics/regression/2dplanes.csv|
|pol|15000|26|0.90MB|OPENML Pole Telecom Dataset|analytics/regression/pole_telecomm/pol_all.csv|
|solar|1066|9|0.02MB|UCI Solar Flare Dataset|analytics/regression/solar/flare.data2|
|qsar_47555|1158|51|0.12MB|OPENML QSAR Dataset(47555)|analytics/regression/qsar/qsar_47555.csv|
|qsar_31274|1189|132|0.31MB|OPENML QSAR Dataset(31274)|analytics/regression/qsar/clean_qsar_31274.csv|
|air|999249|18|11.55MB|RITA Airline on-time Performance Dataset (1987 only)|analytics/regression/air_1987_clean.csv.gz|
|buzz_toms|28179|96|1.53MB|UCI Social Media Buzz Dataset - Toms Hardware)|analytics/regression/buzz/TomsHardware.data.gz|
|buzz_twitter|583250|77|31.76MB|UCI Social Media Buzz Dataset - Twitter|analytics/regression/buzz/Twitter.data.gz|
|qsar_47749|6003|610|7.02MB|OPENML QSAR Dataset(47749)|analytics/regression/qsar/qsar_47749.csv|
|olympic2000|66|11|0.00MB|Olympic2000 Dataset from "Analyzing Categorical Data"|analytics/regression/analcatdata_olympic2000.csv|
|qsar_191|4442|1023|8.71MB|OPENML QSAR Dataset(191)|analytics/regression/qsar/qsar_191.csv|
|qsar_33511|6003|420|4.85MB|OPENML QSAR Dataset(33511)|analytics/regression/qsar/clean_qsar_33511.csv|
|corn_m5spec_moisture|80|700|0.48MB|NIR of Corn Samples for Standardization Benchmarking Dataset (Moisture)|analytics/regression/corn/corn_m5spec_moisture.tsv|
|corn_m5spec_oil|80|700|0.48MB|NIR of Corn Samples for Standardization Benchmarking Dataset (Oil)|analytics/regression/corn/corn_m5spec_oil.tsv|
|corn_m5spec_protein|80|700|0.48MB|NIR of Corn Samples for Standardization Benchmarking Dataset (Protein)|analytics/regression/corn/corn_m5spec_protein.tsv|
|corn_m5spec_starch|80|700|0.48MB|NIR of Corn Samples for Standardization Benchmarking Dataset (Starch)|analytics/regression/corn/corn_m5spec_starch.tsv|
|qsar_12789|309|1024|0.62MB|OPENML QSAR Dataset(12789)|analytics/regression/qsar/qsar_12789.csv|
|energy_efficiency_1|768|9|0.04MB|UCI Energy Efficiency Dataset(Heating Load)|analytics/regression/energy_efficiency/ENB2012_data.csv|
|energy_efficiency_2|768|9|0.04MB|UCI Energy Efficiency Dataset(Cooling Load)|analytics/regression/energy_efficiency/ENB2012_data.csv|
|cbm_1|11934|14|1.17MB|UCI CBM Dataset(Compressor)|analytics/regression/cbm/data_compressor.csv|
|cbm_2|11934|14|1.17MB|UCI CBM Dataset(Turbine)|analytics/regression/cbm/data_turbine.csv|
|triazines|186|58|0.04MB|Bilkent Triazines Dataset|analytics/regression/TZ.dat|
|cars_kbb|804|17|0.04MB|R Caret Package KBB Price Cars Dataset|analytics/regression/cars_kbb.csv|
|chem|176|57|0.04MB|Applied Predictive Modeling Chemical Manufacturing Dataset|analytics/regression/chemical_manufacturing_process.csv|
|crime_unnorm_autoTheft|2211|102|1.14MB|UCI Communities Crime(unnorm-autoTheft) DataSet |analytics/regression/communities/unnorm/communities_autoTheft.csv|
|crime_unnorm_burgl|2211|102|1.14MB|UCI Communities Crime(unnorm-burgl) DataSet |analytics/regression/communities/unnorm/communities_burgl.csv|
|crime_unnorm_larc|2211|102|1.14MB|UCI Communities Crime(unnorm-larc) DataSet |analytics/regression/communities/unnorm/communities_larc.csv|
|crime_unnorm_nonViol|2117|102|1.09MB|UCI Communities Crime(unnorm-nonViol) DataSet |analytics/regression/communities/unnorm/communities_nonViol.csv|
|crime_unnorm_violent|1993|102|1.03MB|UCI Communities Crime(unnorm-violent) DataSet |analytics/regression/communities/unnorm/communities_violent.csv|
|crime_unnorm_total|1901|102|0.98MB|UCI Communities Crime(unnorm-total) DataSet |analytics/regression/communities/unnorm/communities_total.csv|
|crime_unnorm_arsons|2123|102|1.09MB|UCI Communities Crime(unnorm-arsons) DataSet |analytics/regression/communities/unnorm/communities_arsons.csv|
|crime_unnorm_assault|2201|102|1.13MB|UCI Communities Crime(unnorm-assault) DataSet |analytics/regression/communities/unnorm/communities_assault.csv|
|crime_unnorm_rapes|2006|102|1.03MB|UCI Communities Crime(unnorm-rapes) DataSet |analytics/regression/communities/unnorm/communities_rapes.csv|
|crime_unnorm_murd|2214|102|1.13MB|UCI Communities Crime(unnorm-murd) DataSet |analytics/regression/communities/unnorm/communities_murd.csv|
|crime_unnorm_robbb|2213|102|1.14MB|UCI Communities Crime(unnorm-robbb) DataSet |analytics/regression/communities/unnorm/communities_robbb.csv|
|ailerons|13750|40|2.31MB|Ailerons Dataset|analytics/regression/ailerons/ailerons_all.csv|
|elevators|16599|18|1.51MB|Elevators Dataset|analytics/regression/dataset_2202_elevators.csv|
|transcoding|68784|19|7.19MB|UCI Video Transcoding Dataset|analytics/regression/transcoding_measurement.csv|
|sol_1|1267|228|1.81MB|Applied Predictive Modeling Solubility Dataset|analytics/regression/solubility/sol.csv|
|sol_2|632|228|0.41MB|Applied Predictive Modeling Solubility Dataset(trans)|analytics/regression/solubility/solTrans.csv|
|blood_brain|208|127|0.18MB|Applied Predictive Modeling Blood Brain Barrier Dataset|analytics/regression/blood_brain.csv|
|aquatic_tox_1|322|23|0.03MB|R QSARData Package Aquatic Toxicity Dataset(lcalc)|analytics/regression/aquatic_tox/aquatic_tox_lcalc.csv|
|aquatic_tox_3|322|65|0.13MB|R QSARData Package Aquatic Toxicity Dataset(moe3d)|analytics/regression/aquatic_tox/aquatic_tox_moe3d.csv|
|aquatic_tox_4|319|48|0.07MB|R QSARData Package Aquatic Toxicity Dataset(qprop)|analytics/regression/aquatic_tox/aquatic_tox_qprop.csv|
|aquatic_tox_2|322|220|0.31MB|R QSARData Package Aquatic Toxicity Dataset(moe2d)|analytics/regression/aquatic_tox/aquatic_tox_moe2d.csv|
|cox2|462|205|0.49MB|R Caret Package Cox2 Dataset|analytics/regression/cox2.csv|
|melting_point|4401|203|6.97MB|R QSARData Package Melting Point Dataset|analytics/regression/melting_point.csv|
|aloi|108000|128|1.74MB|OPENML Aloi Dataset|analytics/regression/aloi.csv.gz|
|nci_60_90th_1|59|3489|1.20MB|NCI-60 Dataset(target: KRT18)|analytics/regression/nci-60/90th_1.csv|
|nci_60_90th_2|59|3489|1.20MB|NCI-60 Dataset(target: KRT19)|analytics/regression/nci-60/90th_2.csv|
|nci_60_90th_3|59|3489|1.20MB|NCI-60 Dataset(target: KRT7)|analytics/regression/nci-60/90th_3.csv|
|nci_60_90th_4|59|3489|1.20MB|NCI-60 Dataset(target: TP53_26_GBL00064)|analytics/regression/nci-60/90th_4.csv|
|nci_60_90th_5|59|3489|1.20MB|NCI-60 Dataset(target: VASP)|analytics/regression/nci-60/90th_5.csv|
|nci_60_90th_6|59|3489|1.20MB|NCI-60 Dataset(target: MSN_4)|analytics/regression/nci-60/90th_6.csv|
|nci_60_90th_7|59|3489|1.20MB|NCI-60 Dataset(target: CDKN2A)|analytics/regression/nci-60/90th_7.csv|
|nci_60_90th_8|59|3489|1.20MB|NCI-60 Dataset(target: KRT8)|analytics/regression/nci-60/90th_8.csv|
|nci_60_90th_9|59|3489|1.20MB|NCI-60 Dataset(target: TP53_10_24342)|analytics/regression/nci-60/90th_9.csv|
|qsar_36276|6003|39|0.88MB|OPENML QSAR Dataset(36726)|analytics/regression/qsar/qsar_36276.csv|
|qsar_47652|1731|83|0.29MB|OPENML QSAR Dataset(47652)|analytics/regression/qsar/qsar_47652.csv|
|blog_feedback|52397|142|21.81MB|UCI Blog Feedback Dataset|analytics/regression/blog_feedback/clean_blogData_train.csv|
|online_news_pop|39644|58|18.48MB|UCI Mashable Online News Popularity Dataset|analytics/regression/online_news_pop/OnlineNewsPopularity.csv|
|ct_slice|53500|379|16.88MB|UCI CT Axis Prediction Dataset|analytics/regression/ct_slice_localization_data.csv.gz|
|loan_default|105471|769|604.10MB|Loan Default Prediction Dataset from Kaggle|analytics/regression/loan_default_prediction/clean_train_v2_imputed.csv.gz|
