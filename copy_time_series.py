marker_pos = ['o','.']
import pandas as pd

import numpy as np
import operator
import matplotlib
try:
    from . import bema 
except:
    import bema
from bema.calc.modeler_calc import ModelerCalc
import matplotlib.pyplot as plt

from math import floor
import numpy as np

bluish = '#4ABDAC'
watermelon = '#FC4A1A'

pd.set_option('display.expand_frame_repr', True)
for ball_id in ballfield_ids:
#     print("BALLFIELD " + str(ball_id))
#     print("FROM " + str(temp[ball_id]['billing_period_start_date'].min()) + " TO " + str(temp[ball_id]['billing_period_start_date'].max()) )

    for row in range(len(temp[ball_id])):
        if temp[ball_id].loc[row,'reading_type'] == 'A':
            temp[ball_id].loc[row,'estimated'] = 0
        else:
            temp[ball_id].loc[row,'estimated'] = 1
        temp[ball_id].loc[row,'marker_pos'] =  marker_pos[int(temp[ball_id].loc[row,'estimated'])]
    #print(gas_files[ferry].head())
    
    
    fig, axes = plt.subplots(nrows=1, ncols=1)

    ax2 = temp[ball_id].plot(x='billing_period_start_date',y='calendarized_allocated_consumption',ax=axes,figsize=(20,15),color=watermelon,alpha=0.5,linewidth=10)

    temp1 = pd.DataFrame()
    temp1 = temp[ball_id][temp[ball_id]['estimated'] == 1]
    if len(temp1) > 0: 
        ax1 = temp1.plot(x='billing_period_start_date',y='calendarized_allocated_consumption',ax=axes,style='.',ms=30, c='darkred')

#     #plt.scatter(x=raw_gas['start_date'].values,y=raw_gas['usage'].values)  
    plt.ylim(ymin=0)   
#     #
#     #plt.ylim(ymax = y_max)
    ax2.set_ylabel('Energy per month [kWh/month]',fontsize=30)
    ax2.set_xlabel('Billing Start Date',fontsize=30)

    ax2.tick_params(labelsize=30,grid_alpha=1)
    ax2.grid(color='r', linestyle='-', linewidth=1, alpha=0.3)
#     #fig.suptitle('Natural Gas Consumption for FDNY Fleet' ,fontsize=20, y= 0.92)
#     #     axes.legend(['BEMA 4P model','Allocated consumption'],fontsize=15)
#     axes.legend(['Hourly meter data','Weekly average'],fontsize=40)
    axes.legend(['Allocated Consumption','estimated'],fontsize=30,loc=1)
    fig.suptitle('Field ' + str(ball_id) + ' monthly electricity consumption Time Series',fontsize=35, y= 0.95)
    plt.savefig('ballfield_time_Series' + str(ball_id)+'.png')
    plt.show()
    




    
