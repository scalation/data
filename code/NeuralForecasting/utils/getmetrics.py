def getmetrics(main_output, actual, forecasts):
    print("Normalized test {}".format(main_output))
    print('N:{}, MSE:{}, MAE:{}, sMAPE:{}'.format(len(actual),
                                                  ('%.3f' %mse(actual, forecasts)),
                                                  ('%.3f' %mae(actual, forecasts)),
                                                  ('%.3f' %smape(actual, forecasts))))
    return
