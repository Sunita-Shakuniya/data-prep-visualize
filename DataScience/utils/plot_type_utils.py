from .plot_show_utils import *
def suggest_plot(combination, data):
    if len(combination) == 2:
        x_column, y_column = combination
        x_dtype = data[x_column].dtype
        print(x_dtype)
        y_dtype = data[y_column].dtype
        print(y_dtype)
        # Suggest a plot based on column types
        if (x_dtype == 'object' and y_dtype == 'int64') or(x_dtype == 'bool' and y_dtype == 'int64') or(x_dtype == 'int64' and y_dtype == 'category') or (x_dtype == 'category' and y_dtype == 'int64')or(x_dtype == 'object' and y_dtype == 'float64') or (x_dtype == 'bool' and y_dtype == 'category') or(x_dtype == 'category' and y_dtype == 'bool'):
            return 'bar plot'  # all possible combination
        elif x_dtype == 'object' and y_dtype == 'object':
            return 'cluster bar plot' #all possible combination
        elif (x_dtype == 'datetime64' and y_dtype == 'bool') or (x_dtype == 'bool' and y_dtype == 'datetiem64') or (x_dtype == 'float' and y_dtype == 'bool') or  (x_dtype == 'int64' and y_dtype == 'bool') or (x_dtype == 'bool' and y_dtype == 'int64') or (x_dtype == 'bool' and y_dtype == 'float64') or (x_dtype == 'object' and y_dtype == 'bool') or (x_dtype == 'bool' and y_dtype == 'object'):
            return 'strip plot' # all posible combination
        elif (x_dtype == 'object' and y_dtype == 'category') or (x_dtype == 'category' and y_dtype == 'object'):
            return 'count' # all posible combination
        elif x_dtype == 'datetime64' and y_dtype == 'datetime64':
            return 'joint plot'
        elif x_dtype == 'float64' and y_dtype == 'category':
            return 'swarm plot'
        elif x_dtype == 'category' and y_dtype == 'datetime64':
            return 'heatmap'
        elif ((x_dtype == 'int64' or x_dtype == 'object')and y_dtype == 'datetime64') or (x_dtype == 'datetime64' and (y_dtype == 'int64' or y_dtype == 'object'))or (x_dtype == 'datetime64' and y_dtype == 'category'):
            return 'line plot' # all posible combination
        elif (x_dtype == 'bool' and y_dtype == 'bool') or (x_dtype == 'category' and y_dtype == 'category'):
            return 'stacked bar plot' # all posible combination
        elif (x_dtype == 'category' and y_dtype == 'float64'):
            return 'strip' # all posible combination
        elif (x_dtype == 'float64' and y_dtype == 'datetime64') or (x_dtype == 'int64' and y_dtype == 'datetime64'):
            return 'time series plot' # all posible combination
        else:
            return 'hexabin plot'  # For numerical data, suggest a scatter plot
    elif len(combination) == 3:
        x_column, y_column, z_column = combination
        x_dtype = data[x_column].dtype
        print(x_dtype)
        y_dtype = data[y_column].dtype
        print(y_dtype)
        z_dtype = data[z_column].dtype
        print(z_dtype)
        # Suggest a plot based on column types
        if x_dtype == 'int64' and y_dtype == 'float64' and z_dtype == 'object':
            return '3d bar plot'  #all possiable combination
        elif (x_dtype == 'datetime64' or y_dtype == 'datetime64' or z_dtype == 'datetime64'):
            return '3d line plot with time series'  # all possible combination
        elif (x_dtype == 'bool' or y_dtype == 'bool' or z_dtype == 'bool') or (x_dtype == 'category' or y_dtype == 'category' or z_dtype == 'category') :    
            return 'grouped bar plot' # possible combination
        elif (x_dtype == 'int64' and y_dtype == 'int64' and z_dtype == 'float64') or (x_dtype == 'int64' and y_dtype == 'object' and z_dtype == 'int64') or (x_dtype == 'float64' and y_dtype == 'int64' and z_dtype == 'datetime64') or (x_dtype == 'object' and y_dtype == 'int64' and z_dtype == 'int64') or (x_dtype == 'int64' and y_dtype == 'int64' and z_dtype == 'float64') or (x_dtype == 'object' and y_dtype == 'int64' and z_dtype == 'object'):
            return '3d line plot'  # all possible combination
        elif x_dtype == 'int64' and y_dtype == 'datetime64' and z_dtype == 'bool':
            return '3d scatter plot with time series and boolean coloring' #all possible combination
        elif (x_dtype == 'int64' and y_dtype == 'int64' and z_dtype == 'object') or (x_dtype == 'float64' and y_dtype == 'object' and z_dtype == 'int64') or (x_dtype == 'float64' and y_dtype == 'object' and z_dtype == 'float64') or (x_dtype == 'float64' and y_dtype == 'object' and z_dtype == 'object'):
            return '3d stacked bar plot' # possible combination
        elif (x_dtype == 'int64' and y_dtype == 'float64' and z_dtype == 'int64') or (x_dtype == 'int64' and y_dtype == 'float64' and z_dtype == 'float64') or (x_dtype == 'int64' and y_dtype == 'object' and z_dtype == 'float64') or (x_dtype == 'float64' and y_dtype == 'int64' and z_dtype == 'int64') or (x_dtype == 'float64' and y_dtype == 'int64' and z_dtype == 'float64') or (x_dtype == 'float64' and y_dtype == 'int64' and z_dtype == 'object')  :
            return '3d surface plot'
        elif (x_dtype == 'int64' and y_dtype == 'int64' and z_dtype == 'bool') or (x_dtype == 'int64' and y_dtype == 'float64' and z_dtype == 'bool') or (x_dtype == 'int64' and y_dtype == 'object' and z_dtype == 'bool'):     
            return 'bubble plot with boolean encoding' # possible combination
        elif x_dtype == 'int64' and y_dtype == 'int64' and z_dtype == 'category':
            return 'seaborn strip plot' #all possible combination
        else:
            return '3d scatter plot'  # For numerical data, suggest a 3D scatter plot
    else:
        return '3d scatter plot'  # Default to scatter plot if combination length is not 2 or 3


def generate_2dplot(plot_type, data, x_column, y_column):
    if plot_type == 'bar plot':
        fig = generate_bar_plot(data, x=x_column, y=y_column,  title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'cluster bar plot':
        fig = generate_cluster_bar_plot(data, x=x_column, y=y_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'strip plot':
        fig = generate_strip_plot(data, x=x_column, y=y_column,  title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'count':
        fig = generate_count(data, x=x_column, y=y_column,  title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'histogram plot':
        fig = generate_histogram_plot(data, x=x_column, y=y_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'joint plot':
        fig = generate_joint_plot(data, x=x_column, y=y_column,  title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'heatmap':
        fig = generate_heatmap(data, x=x_column, y=y_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'line plot':
        fig = generate_line_plot(data, x=x_column, y=y_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'stacked bar plot':
        fig = generate_stacked_bar_plot(data, x=x_column, y=y_column,title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'swarm':
        fig = generate_swarm(data, x=x_column, y=y_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'strip':
        fig = generate_strip(data, x=x_column, y=y_column,title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    elif plot_type == 'time series plot':
        fig = generate_time_series_plot(data, x=x_column, y=y_column,title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    else:
        plot_type == 'hexabin plot'
        fig = generate_hexabin_plot(data, x=x_column, y=y_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}')
    return fig

def generate_3dplot(plot_type, data, x_column, y_column, z_column):
    if plot_type == '3d bar plot':
        fig = generate_3d_bar_plot(data, x=x_column, y=y_column, z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == '3d line plot with time series':
        fig = generate_3d_line_plot_time_series(data, x=x_column, y=y_column, z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == 'grouped bar plot':
        fig = generate_grouped_bar_plot(data, x=x_column, y=y_column, z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == '3d line plot':
        fig = generate_3d_line_plot(data, x=x_column, y=y_column, z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == '3d scatter plot with time series and boolean coloring':
        fig = generate_scatter_plot_time_series_boolean_coloring(data, x=x_column, y=y_column, z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == '3d stacked bar plot':
        fig = generate_3d_stacked_bar_plot(data, x=x_column, y=y_column, z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == 'bubble plot with boolean encoding':
        fig = generate_bubble_plot_boolean_encoding(data, x=x_column, y=y_column,z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    elif plot_type == 'seaborn strip plot':
        fig = generate_seaborn_strip_plot(data, x=x_column, y=y_column, z=z_column,title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    else:
        plot_type == '3d scatter plot'
        fig = generate_scatter_plot(data, x=x_column, y=y_column,z=z_column, title=f'{plot_type.capitalize()} Plot: {x_column}, {y_column}, {z_column}')
    return fig