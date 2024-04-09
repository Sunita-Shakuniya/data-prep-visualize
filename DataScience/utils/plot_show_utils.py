import plotly.graph_objects as go
import matplotlib.cm as cm
import pandas as pd
import matplotlib.colors as mcolors
import plotly.express as px
import numpy as np
'''
def generate_line_plot(data, x, y, title=''):
    fig = go.Figure(data=go.Scatter(x=data[x], y=data[y], mode='lines'))
    fig.update_layout(title=title)
    return fig

def generate_bar_plot(data, x, y, title=''):
    fig = go.Figure(data=go.Bar(x=data[x], y=data[y]))
    fig.update_layout(title=title)
    return fig
'''
def generate_color_palette(categories):
    """
    Generate a color palette based on unique categories.

    Parameters:
        - categories (list): A list of unique categories.

    Returns:
        - colors (list): A list of colors corresponding to the unique categories.
    """
    # Define the default color combination
    default_colors = ['#6235D1', '#3B00A8', '#49C8FF', '#0080A8', '#0A4A94', '#0A4A94', '#528FD6' ]
     # Calculate the number of repetitions needed for the default colors
    repetitions = len(categories) // len(default_colors) + 1
    # Generate the color palette based on unique categories
    colors = [default_colors[i % len(default_colors)] for i in range(len(categories) * repetitions)]
    
    return colors
#=======================================================================
def generate_bar_plot(data, x, y, title=''):
    # Get unique categories in x_data
    unique_categories = data[x]

    # Generate colors based on the unique categories
    colors = generate_color_palette(unique_categories)

    # Create bar trace
    bar_trace = go.Bar(x=data[x], y=data[y], marker=dict(color=colors))
    
    # Create layout
    layout = go.Layout(
        title=title,
        xaxis=dict(title=x),
        yaxis=dict(title=y)
    )

    # Create figure
    fig = go.Figure(bar_trace, layout)

    return fig

def generate_cluster_bar_plot(data, x, y, title=''):
    # Clean and preprocess the data
    data[x] = data[x].str.strip().str.lower()
    data = data.drop_duplicates()
    
    # Group data by x column and sum the values in y column
    grouped_data = data.groupby(x)[y].count().reset_index()

    # Define custom list of colors
    custom_colors = ['#6235D1', '#3B00A8', '#49C8FF', '#0080A8', '#0A4A94', '#0A4A94', '#528FD6']

    # Create bar trace for each category in x
    bar_traces = []
    for index, row in grouped_data.iterrows():
        color_index = index % len(custom_colors)  # Use modulo to handle cases where colors run out
        bar_trace = go.Bar(x=[row[x]], y=[row[y]], name=row[x], marker=dict(color=custom_colors[color_index]))
        bar_traces.append(bar_trace)

    # Create layout
    layout = go.Layout(
        title=title,
        xaxis=dict(title=x),
        yaxis=dict(title=y),
        barmode='group'  # Set barmode to 'group' for clustered bar plot
    )

    # Create figure
    fig = go.Figure(data=bar_traces, layout=layout)

    return fig
def generate_strip_plot(data, x, y, title=''):
    # Check if x variable is boolean
    if data[x].dtype == 'bool':
        bool_variable = 'x'
    # Check if y variable is boolean
    elif data[y].dtype == 'bool':
        bool_variable = 'y'
    else:
        raise ValueError("Neither x nor y is a boolean variable.")

    if bool_variable == 'x':
        # Generate colors based on unique categories in the x variable
        unique_categories = data[x].unique()
        colors = generate_color_palette(unique_categories)
        
        # Create strip plot with boolean variable on the x-axis
        fig = go.Figure()
        for index, row in data.iterrows():
            fig.add_trace(go.Scatter(x=[row[x]], y=[row[y]], mode='markers', marker=dict(color=colors[index]), name=row[x]))
        fig.update_layout(title=title, xaxis_title=x, yaxis_title=y)
    elif bool_variable == 'y':
        # Generate colors based on unique categories in the y variable
        unique_categories = data[y].unique()
        colors = generate_color_palette(unique_categories)
        
        # Create strip plot with boolean variable on the y-axis
        fig = go.Figure()
        for index, row in data.iterrows():
            fig.add_trace(go.Scatter(x=[row[y]], y=[row[x]], mode='markers', marker=dict(color=colors[index]), name=row[y]))
        fig.update_layout(title=title, xaxis_title=y, yaxis_title=x)

    return fig

def generate_count(data, x, y, title=''):
    if data[x].dtype == 'object':
        # Generate colors based on unique categories in the y variable
        unique_categories = data[y].unique()
        colors = generate_color_palette(unique_categories)
        
        # Generate strip plot
        fig = px.strip(data, x=x, title=title, color=y, color_discrete_sequence=colors)

        # Update layout
        fig.update_layout(
            xaxis_title=x,
            yaxis_title='Count'
        )
    else:
        # Swap x and y
        # Generate colors based on unique categories in the x variable
        unique_categories = data[x].unique()
        colors = generate_color_palette(unique_categories)
        
        fig = px.strip(data, x=y, y=x, title=title, color=x, color_discrete_sequence=colors)

        # Update layout
        fig.update_layout(
            xaxis_title=y,
            yaxis_title='Count'
        )

    return fig

def generate_histogram_plot(data, x, y, title=''):
    # Get unique categories in x_data
    unique_categories = data[x]

    # Generate colors based on the unique categories
    colors = generate_color_palette(unique_categories)

    # Create bar trace
    bar_trace = go.Bar(x=data[x], y=data[y], marker=dict(color=colors))
    
    # Create layout
    layout = go.Layout(
        title=title,
        xaxis=dict(title= x),
        yaxis=dict(title=y)
    )

    # Create figure
    fig = go.Figure(bar_trace, layout)

    return fig

def generate_joint_plot(data, x, y, title=''):
    # Get unique categories in x_data
    unique_categories = data[x]

    # Generate colors based on the unique categories
    colors = generate_color_palette(unique_categories)

    # Create bar trace
    bar_trace = go.Bar(x=data[x], y=data[y], marker=dict(color=colors))
    
    # Create layout
    layout = go.Layout(
        title=title,
        xaxis=dict(title=x),
        yaxis=dict(title=y)
    )

    # Create figure
    fig = go.Figure(bar_trace, layout)

    return fig

def generate_heatmap(data, x, y, title=''):
    # Generate colors based on unique categories
    unique_categories = data[x].unique()
    colors = generate_color_palette(unique_categories)
    
    fig = px.imshow(data, x=x, y=y, title=title, color_continuous_scale=colors)
    fig.update_xaxes(title=x)
    fig.update_yaxes(title=y)
    
    return fig

def generate_line_plot(data, x, y, title=''):
    colors = generate_color_palette(data[x].unique())  # Assuming x is categorical
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[x], y=data[y], mode='lines', name=y, line=dict(color=colors[0])))
    fig.update_layout(title=title, xaxis_title=x, yaxis_title=y)
    return fig

def generate_stacked_bar_plot(data, x, y, title=''):
    # Group data by x column and y column
    grouped_data = data.groupby([x, y]).size().unstack(fill_value=0).reset_index()

    # Get unique categories in y column
    categories = grouped_data.columns.drop(x)

    # Generate colors based on unique categories
    colors = generate_color_palette(categories)

    # Create stacked bar traces
    bar_traces = []
    for i, color in enumerate(colors):
        bar_trace = go.Bar(x=grouped_data[x], y=grouped_data[categories[i]], name=categories[i], marker=dict(color=color))
        bar_traces.append(bar_trace)

    # Create layout
    layout = go.Layout(
        title=title,
        xaxis=dict(title=x),
        yaxis=dict(title='Count'),
        barmode='stack'  # Set barmode to 'stack' for stacked bar plot
    )

    # Create figure
    fig = go.Figure(data=bar_traces, layout=layout)

    return fig

def generate_swarm(data, x, y, title=''):
    # Generate colors based on unique categories
    unique_categories = data[x].unique()
    colors = generate_color_palette(unique_categories)
    
    fig = px.swarm(data, x=x, y=y, title=title, color=x, color_discrete_sequence=colors)
    fig.update_xaxes(title=x)
    fig.update_yaxes(title=y)
    
    return fig

def generate_strip(data, x, y, title=''):
    # Generate colors based on unique categories
    unique_categories = data[x].unique()
    colors = generate_color_palette(unique_categories)

    # Generate strip plot
    fig = px.strip(data, x=x, y=y, title=title, color=x, color_discrete_sequence=colors)

    # Update layout
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y
    )

    return fig

def generate_time_series_plot(data, x, y, title=''):
    # Generate colors based on unique categories in the y variable
    unique_categories = data[y].unique()
    colors = generate_color_palette(unique_categories)

    fig = go.Figure()

    # Add scatter trace for time series data
    for category, color in zip(unique_categories, colors):
        category_data = data[data[y] == category]
        fig.add_trace(go.Scatter(x=category_data[x], y=category_data[y], mode='lines', name=category, line=dict(color=color)))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title=x,
        yaxis_title=y
    )

    return fig

#________________________________________________NOT USED
def generate_2d_density_plot(data, x, y, title=''):
    # Generate color palette based on unique categories in the x variable
    unique_categories_x = data[x].unique()
    colors_x = generate_color_palette(unique_categories_x)

    # Generate color palette based on unique categories in the y variable
    unique_categories_y = data[y].unique()
    colors_y = generate_color_palette(unique_categories_y)

    fig = px.density_heatmap(data, x=x, y=y, title=title, color_continuous_scale=colors_x, color_continuous_midpoint=0)
    return fig

def generate_hexabin_plot(data, x, y, title=''):
    # Convert x to a categorical variable
    data[x] = pd.Categorical(data[x])
    # Generate color palette based on unique categories in the x variable    
    unique_categories = data[x].unique()
    colors = generate_color_palette(unique_categories)
    
    fig = px.scatter(data_frame=data, x=x, y=y, title=title, color_discrete_sequence=colors)
    fig.update_traces(marker=dict(symbol='hexagon', line=dict(width=0)))
    fig.update_layout(showlegend=False)
    return fig
#=================================================================================
def generate_color_palette2(categories):
    # Generate a colormap with the same number of colors as unique categories
    #colormap = cm.get_cmap('viridis', len(categories))
    
    # Generate colors based on the colormap
    #colors = [mcolors.to_hex(colormap(i)) for i in range(len(categories))]
    # Define the default color combination
    default_colors = ['#6235D1', '#3B00A8', '#49C8FF', '#0080A8', '#0A4A94', '#0A4A94', '#528FD6']

    # Generate the color palette based on unique categories
    colors = [default_colors[i % len(default_colors)] for i in range(len(categories))]
    
    return colors

def generate_3d_bar_plot(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    # Get unique categories in x_data
    unique_categories = data[x]

    # Generate colors based on the unique categories
    colors = generate_color_palette2(unique_categories)
    
    # Create 3D bar traces
    bar_traces = []
    for i in range(len(data[x]) - 1):
        bar_trace = go.Mesh3d(
            x=[data[x][i], data[x][i], data[x][i+1], data[x][i+1]],
            y=[data[y][i], data[y][i+1], data[y][i+1], data[y][i]],
            z=[0, 0, data[z][i], data[z][i]],
            color=colors[i],  # Selecting color based on index
            opacity=0.7
        )
        bar_traces.append(bar_trace)

    # Create layout
    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis=dict(title=x),
            yaxis=dict(title=y),
            zaxis=dict(title=z),
        )
    )

    # Create figure
    fig = go.Figure(data=bar_traces, layout=layout)

    return fig

def generate_3d_line_plot_time_series(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    fig = go.Figure()

    unique_x = data[x].unique()
    unique_y = data[y].unique()
    unique_z = data[z].unique()

    colors = generate_color_palette2(unique_x)

    for i, x_val in enumerate(unique_x):
        for j, y_val in enumerate(unique_y):
            for k, z_val in enumerate(unique_z):
                group_data = data[(data[x] == x_val) & (data[y] == y_val) & (data[z] == z_val)]
                if not group_data.empty:
                    fig.add_trace(go.Scatter3d(
                        x=[x_val],
                        y=[y_val],
                        z=[z_val],
                        dx=0.8, dy=0.8, dz=[group_data[z].sum()],
                        opacity=0.7,
                        name=f"{x_val}-{y_val}-{z_val}",
                        marker=dict(color=colors[i])
                    ))

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title=x,
            yaxis_title=y,
            zaxis_title=z
        )
    )

    return fig


def generate_grouped_bar_plot(data, x, y, z, title=''):
    fig = go.Figure()

    unique_x = data[x].unique()
    unique_y = data[y].unique()
    unique_z = data[z].unique()

    colors = generate_color_palette2(unique_x)

    for i, x_val in enumerate(unique_x):
        for j, y_val in enumerate(unique_y):
            for k, z_val in enumerate(unique_z):
                group_data = data[(data[x] == x_val) & (data[y] == y_val) & (data[z] == z_val)]
                if not group_data.empty:
                    fig.add_trace(go.Scatter3d(
                        x=group_data[x],
                        y=group_data[y],
                        z=group_data[z],
                        mode='lines',
                        line=dict(color=colors[i]),
                        name=f"{x_val}-{y_val}-{z_val}"
                    ))

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title=x,
            yaxis_title=y,
            zaxis_title=z
        )
    )

    return fig


def generate_3d_line_plot(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    fig = go.Figure()

    unique_x = data[x].unique()
    unique_y = data[y].unique()
    unique_z = data[z].unique()

    colors = generate_color_palette2(unique_x)

    for i, x_val in enumerate(unique_x):
        for j, y_val in enumerate(unique_y):
            for k, z_val in enumerate(unique_z):
                group_data = data[(data[x] == x_val) & (data[y] == y_val) & (data[z] == z_val)]
                if not group_data.empty:
                    fig.add_trace(go.Scatter3d(
                        x=group_data[x],
                        y=group_data[y],
                        z=group_data[z],
                        mode='lines',
                        line=dict(color=colors[i]),
                        name=f"{x_val}-{y_val}-{z_val}"
                    ))

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title=x,
            yaxis_title=y,
            zaxis_title=z
        )
    )

    return fig



def generate_scatter_plot_time_series_boolean_coloring(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    # Identify the boolean column dynamically
    boolean_columns = [col for col in [x, y, z] if data[col].dtype == bool]
    if not boolean_columns:
        raise ValueError("No boolean columns found among x, y, z columns.")

    # Choose the first boolean column found
    boolean_column = boolean_columns[0]

    # Get unique categories in the boolean column
    unique_categories = data[boolean_column].unique()

    # Generate colors based on the unique categories
    colors = generate_color_palette2(unique_categories)

    # Create a figure
    fig = go.Figure()

    # Add traces for each unique value of the boolean column
    for value, color in zip(unique_categories, colors):
        # Filter data for the current boolean value
        filtered_data = data[data[boolean_column] == value]

        # Add scatter trace
        fig.add_trace(go.Scatter3d(
            x=filtered_data[x],
            y=filtered_data[y],
            z=filtered_data[z],
            mode='markers',
            marker=dict(
                color=color,  # Use color from palette
                opacity=0.7,
                size=8,
                line=dict(width=0.5, color='Black')
            ),
            name=str(value)  # Convert boolean value to string for legend
        ))

    # Update layout
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title=x,
            yaxis_title=y,
            zaxis_title=z,
        ),
        legend_title=boolean_column,
        showlegend=True
    )

    return fig
def generate_3d_stacked_bar_plot(data, x, y, z, title=''):
# Group data by x and y columns and sum z values
    # Group data by x and y columns and sum z values
    grouped_data = data.groupby([x, y])[z].sum().reset_index()

    # Get unique categories in y data
    unique_categories = grouped_data[y].unique()

    # Generate colors based on unique categories
    colors = generate_color_palette2(unique_categories)

    # Create 3D stacked bar traces for each category
    bar_traces = []
    for i, category in enumerate(unique_categories):
        category_data = grouped_data[grouped_data[y] == category]
        bar_trace = go.Bar(
            x=category_data[x],
            y=category_data[z],
            name=str(category),
            marker=dict(color=colors[i % len(colors)])  # Use colors from palette
        )
        bar_traces.append(bar_trace)

    # Create layout
    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis=dict(title=x),
            yaxis=dict(title='Stack'),
            zaxis=dict(title=z),
        ),
        barmode='stack'
    )

    # Create figure
    fig = go.Figure(data=bar_traces, layout=layout)

    return fig

def generate_bubble_plot_boolean_encoding(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    # Get unique categories in the z column
    unique_categories = data[z].unique()

    # Generate colors based on unique categories
    colors = generate_color_palette2(unique_categories)

    # Create figure
    fig = go.Figure()

    # Add scatter3d trace
    for category, color in zip(unique_categories, colors):
        category_data = data[data[z] == category]
        fig.add_trace(go.Scatter3d(
            x=category_data[x],
            y=category_data[y],
            z=category_data[z],
            mode='markers',
            marker=dict(
                size=10,  # Set the size of the bubbles
                color=color,  # Set the color based on the category
                opacity=0.7,
            ),
            name=str(category)
        ))

    # Update layout
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title=x,
            yaxis_title=y,
            zaxis_title=z,
        )
    )

    return fig

def generate_seaborn_strip_plot(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    # Get unique categories in x_data
    unique_categories = data[x]

    # Generate colors based on the unique categories
    colors = generate_color_palette2(unique_categories)
    
    # Create 3D bar traces
    bar_traces = []
    for i in range(len(data[x]) - 1):
        bar_trace = go.Mesh3d(
            x=[data[x][i], data[x][i], data[x][i+1], data[x][i+1]],
            y=[data[y][i], data[y][i+1], data[y][i+1], data[y][i]],
            z=[0, 0, data[z][i], data[z][i]],
            color=colors[i],  # Selecting color based on index
            opacity=0.7
        )
        bar_traces.append(bar_trace)

    # Create layout
    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis=dict(title=x),
            yaxis=dict(title=y),
            zaxis=dict(title=z),
        )
    )

    # Create figure
    fig = go.Figure(data=bar_traces, layout=layout)

    return fig

def generate_scatter_plot(data, x, y, z, title=''):
    """
    Generate a 3D bar plot using Plotly.

    Parameters:
        - data (dict): A dictionary containing the data for x, y, and z columns.
        - x (str): The name of the column to be used as x-axis values.
        - y (str): The name of the column to be used as y-axis values.
        - z (str): The name of the column to be used as z-axis values.
        - title (str): The title of the plot.

    Returns:
        - fig (go.Figure): The Plotly figure object.
    """
    # Get unique categories in the z data
    unique_categories = data[z].unique()

    # Generate colors based on unique categories
    colors = generate_color_palette2(unique_categories)

    # Assign color based on the z values
    data['color'] = data[z].apply(lambda val: colors[unique_categories.tolist().index(val)])

    # Create the scatter trace
    trace = go.Scatter3d(
        x=data[x],
        y=data[y],
        z=data[z],
        mode='markers',
        marker=dict(
            size=8,
            opacity=0.7,
            color=data['color'],  # Color based on z values
        ),
    )

    # Create layout
    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis=dict(title=x),
            yaxis=dict(title=y),
            zaxis=dict(title=z),
        )
    )

    # Create figure
    fig = go.Figure(data=[trace], layout=layout)

    return fig