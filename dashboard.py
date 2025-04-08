# import psutil
# import time
# import dash
# from dash import dcc, html, dash_table
# from dash.dependencies import Input, Output
# import plotly.graph_objs as go
# from collections import deque
# import pandas as pd  # Import pandas for DataFrame operations

# # Initialize Dash app
# app = dash.Dash(__name__)
# app.title = "Real-Time CPU and Memory Usage"

# # Initialize data structures for storing real-time data
# cpu_history = deque(maxlen=50)  # Store the last 50 data points
# memory_history = deque(maxlen=50)
# timestamps = deque(maxlen=50)

# # Initialize a counter for time (seconds)
# time_counter = 0

# # Layout of the dashboard
# app.layout = html.Div([
#     html.H1("Real-Time CPU and Memory Usage", style={'textAlign': 'center'}),
    
#     html.Div([
#         html.Div([
#             dcc.Graph(id="cpu-graph", style={'height': '300px'}),
#             html.Div(id="cpu-status", style={'textAlign': 'center', 'color': 'blue', 'fontSize': '18px'}),
#         ], style={'flex': '1', 'padding': '10px'}),
        
#         html.Div([
#             dcc.Graph(id="memory-graph", style={'height': '300px'}),
#             html.Div(id="memory-status", style={'textAlign': 'center', 'color': 'green', 'fontSize': '18px'}),
#         ], style={'flex': '1', 'padding': '10px'})
#     ], style={'display': 'flex', 'flexDirection': 'row'}),
    
#     html.Div([
#         html.H3("Processes", style={'textAlign': 'center', 'color': 'black'}),
#         dash_table.DataTable(
#             id="process-table",
#             columns=[
#                 {"name": "Name", "id": "name"},
#                 {"name": "Status", "id": "status"},
#                 {"name": "CPU Usage (%)", "id": "cpu_percent"},
#                 {"name": "Memory Usage (%)", "id": "memory_percent"},
#             ],
#             style_table={'overflowX': 'auto', 'backgroundColor': '#f4f4f9', 'color': 'black'},
#             style_cell={'textAlign': 'left', 'padding': '8px', 'border': '1px solid #ddd'},
#             page_size=10
#         ),
#     ], style={'padding': '20px'}),
    
#     dcc.Interval(id="update-interval", interval=1000, n_intervals=0)  # Interval to update every second
# ], style={'backgroundColor': '#f4f4f9', 'padding': '20px'})

# # Callback to update the CPU graph
# @app.callback(
#     Output("cpu-graph", "figure"),
#     Output("cpu-status", "children"),
#     Input("update-interval", "n_intervals")
# )
# def update_cpu_graph(_):
#     global time_counter
#     # Get CPU usage as an integer (rounded to the nearest whole number)
#     cpu_percent = round(psutil.cpu_percent(interval=0.1))

#     # Increment time_counter for seconds
#     time_counter += 1

#     # Append new data for CPU
#     cpu_history.append(cpu_percent)
#     timestamps.append(time_counter)  # Use time_counter as time in seconds

#     # Create the figure for CPU usage graph
#     figure = {
#         "data": [go.Scatter(x=list(timestamps), y=list(cpu_history), mode="lines", name="CPU Usage (%)", line=dict(color='blue'))],
#         "layout": go.Layout(title="CPU Usage Over Time", xaxis={"title": "Time (s)"}, yaxis={"title": "CPU Usage (%)"}, plot_bgcolor="#ffffff", font={"color": "black"})
#     }

#     # Update CPU status text
#     status_text = f"CPU Usage: {cpu_percent}%"

#     return figure, status_text

# # Callback to update the Memory graph
# @app.callback(
#     Output("memory-graph", "figure"),
#     Output("memory-status", "children"),
#     Input("update-interval", "n_intervals")
# )
# def update_memory_graph(_):
#     global time_counter
#     # Get memory usage
#     memory_percent = psutil.virtual_memory().percent

#     # Increment time_counter for seconds
#     time_counter += 1

#     # Append new data for Memory
#     memory_history.append(memory_percent)
#     timestamps.append(time_counter)  # Use time_counter as time in seconds

#     # Create the figure for Memory usage graph
#     figure = {
#         "data": [go.Scatter(x=list(timestamps), y=list(memory_history), mode="lines", name="Memory Usage (%)", line=dict(color='green'))],
#         "layout": go.Layout(title="Memory Usage Over Time", xaxis={"title": "Time (s)"}, yaxis={"title": "Memory Usage (%)"}, plot_bgcolor="#ffffff", font={"color": "black"})
#     }

#     # Update Memory status text
#     status_text = f"Memory Usage: {memory_percent}%"

#     return figure, status_text

# # Callback to update the Process Table with real-time data
# @app.callback(
#     Output("process-table", "data"),
#     Input("update-interval", "n_intervals")
# )
# def update_process_table(_):
#     # Fetch process information
#     processes = []
#     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
#         try:
#             process_info = proc.info
#             process_info['cpu_percent'] = round(process_info['cpu_percent'], 2)  # Round CPU usage to 2 decimal places
#             process_info['memory_percent'] = round(process_info['memory_percent'], 2)  # Round memory usage to 2 decimal places
#             processes.append(process_info)
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
    
#     # Convert list of processes into a DataFrame
#     df = pd.DataFrame(processes)
    
#     # Return data as a dictionary for the DataTable
#     return df.to_dict('records')

# # Run the app
# if __name__ == "__main__":
#     app.run(debug=True)




# import psutil
# import time
# import os

# # Function to fetch and print process information continuously
# def print_process_info():
#     try:
#         while True:
#             # Clear the terminal screen (for Windows, use 'cls'; for macOS/Linux, use 'clear')
#             os.system('cls' if os.name == 'nt' else 'clear')
            
#             # Print headers
#             print(f"{'Name':<30} {'PID':<10} {'Status':<15} {'CPU%':<10} {'Memory%':<10}")
#             print("="*75)
            
#             # Iterate over all processes
#             for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
#                 try:
#                     # Extract process information
#                     process_info = proc.info
#                     name = process_info['name']
#                     pid = process_info['pid']
#                     status = process_info['status']
#                     cpu_percent = round(process_info['cpu_percent'], 2)
#                     memory_percent = round(process_info['memory_percent'], 2)
                    
#                     # Print the process information in a formatted way
#                     print(f"{name:<30} {pid:<10} {status:<15} {cpu_percent:<10} {memory_percent:<10}")
                
#                 except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#                     # Skip processes that have ended or are inaccessible
#                     continue
            
#             # Wait for 1 second before updating the process information
#             time.sleep(1)
    
#     except KeyboardInterrupt:
#         # Exit gracefully on user interrupt (Ctrl+C)
#         print("\nExiting...")
#         exit()

# # Call the function to print the process information continuously
# print_process_info()



# from dash import dcc, html, dash_table  # Import dash_table from dash
# import psutil
# from dash.dependencies import Input, Output
# import dash

# # Create the Dash app
# app = dash.Dash(__name__)

# # Define layout
# app.layout = html.Div([
#     html.H1("Real-Time Process Information", style={'textAlign': 'center'}),
#     dash_table.DataTable(  # Create a table for displaying process data
#         id='process-table',
#         columns=[
#             {"name": "Process Name", "id": "name"},
#             {"name": "PID", "id": "pid"},
#             {"name": "Status", "id": "status"},
#             {"name": "CPU Percent", "id": "cpu_percent"},
#             {"name": "Memory Percent", "id": "memory_percent"}
#         ],
#         style_table={'height': '400px', 'overflowY': 'auto'},  # Scrollable table
#     ),
#     dcc.Interval(  # Interval to update data every second
#         id='interval-component',
#         interval=1000,  # Update every second (1000 ms)
#         n_intervals=0  # Initial interval count
#     )
# ])

# # Define the callback to update the table with process data
# @app.callback(
#     Output('process-table', 'data'),
#     Input('interval-component', 'n_intervals')
# )
# def update_processes(n_intervals):
#     # Fetch process info using psutil
#     process_info = []
#     for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
#         try:
#             process_info.append(proc.info)  # Append process info to the list
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass

#     return process_info  # Return the data for the table

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)  # Correct method to run the server






# from dash import Dash, html, dcc, Input, Output, State
# import dash
# import plotly.express as px
# import psutil
# from collections import deque
# import time
# from threading import Thread

# app = Dash(__name__)

# cpu_data = deque(maxlen=50)
# memory_data = deque(maxlen=50)
# timestamps = deque(maxlen=50)

# app.layout = html.Div([
#     html.H1("Real-Time Process Monitoring Dashboard"),
#     dcc.Graph(id='cpu-usage-graph'),
#     dcc.Graph(id='memory-usage-graph'),
#     html.Table(id='process-table'),
#     dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
# ])

# def update_data():
#     while True:
#         cpu_usage = psutil.cpu_percent(interval=1)
#         memory_usage = psutil.virtual_memory().percent
#         timestamps.append(time.strftime("%H:%M:%S"))
#         cpu_data.append(cpu_usage)
#         memory_data.append(memory_usage)
#         time.sleep(2)

# Thread(target=update_data, daemon=True).start()

# @app.callback(
#     [Output('cpu-usage-graph', 'figure'),
#      Output('memory-usage-graph', 'figure'),
#      Output('process-table', 'children')],
#     [Input('interval-component', 'n_intervals'),
#      Input({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'n_clicks')],
#     [State({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'id')]
# )
# def update_dashboard(n, n_clicks, button_ids):
#     # Handle process termination
#     if n_clicks and any(n > 0 for n in n_clicks):
#         for i, clicks in enumerate(n_clicks):
#             if clicks > 0:
#                 pid_to_kill = button_ids[i]['index']
#                 try:
#                     psutil.Process(pid_to_kill).terminate()
#                 except psutil.NoSuchProcess:
#                     pass

#     # Update CPU and Memory graphs
#     cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'})
#     memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'})
    
#     # Update process table
#     processes = []
#     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
#         processes.append(html.Tr([
#             html.Td(proc.info['pid']),
#             html.Td(proc.info['name']),
#             html.Td(f"{proc.info['cpu_percent']:.2f}%"),
#             html.Td(f"{proc.info['memory_percent']:.2f}%"),
#             html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0))
#         ]))
    
#     process_table = html.Table([
#         html.Thead(html.Tr([html.Th("PID"), html.Th("Name"), html.Th("CPU (%)"), html.Th("Memory (%)"), html.Th("Action")])),
#         html.Tbody(processes)
#     ])
    
#     return cpu_fig, memory_fig, process_table

# if __name__ == "__main__":
#     app.run(debug=True)



# from dash import Dash, html, dcc, Input, Output, State
# import dash
# import plotly.express as px
# import psutil
# from collections import deque
# import time
# from threading import Thread

# app = Dash(__name__)

# cpu_data = deque(maxlen=50)
# memory_data = deque(maxlen=50)
# timestamps = deque(maxlen=50)

# app.layout = html.Div([
#     html.H1("Real-Time Process Monitoring Dashboard"),
#     dcc.Graph(id='cpu-usage-graph'),
#     dcc.Graph(id='memory-usage-graph'),
#     html.Table(id='process-table'),
#     dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
# ])

# def update_data():
#     while True:
#         cpu_usage = psutil.cpu_percent(interval=1)  # Total CPU usage
#         memory_usage = psutil.virtual_memory().percent
#         timestamps.append(time.strftime("%H:%M:%S"))
#         cpu_data.append(cpu_usage)
#         memory_data.append(memory_usage)
#         time.sleep(2)

# Thread(target=update_data, daemon=True).start()

# @app.callback(
#     [Output('cpu-usage-graph', 'figure'),
#      Output('memory-usage-graph', 'figure'),
#      Output('process-table', 'children')],
#     [Input('interval-component', 'n_intervals'),
#      Input({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'n_clicks')],
#     [State({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'id')]
# )
# def update_dashboard(n, n_clicks, button_ids):
#     # Handle process termination
#     if n_clicks and any(n > 0 for n in n_clicks):
#         for i, clicks in enumerate(n_clicks):
#             if clicks > 0:
#                 pid_to_kill = button_ids[i]['index']
#                 try:
#                     psutil.Process(pid_to_kill).terminate()
#                 except psutil.NoSuchProcess:
#                     pass

#     # Update CPU and Memory graphs
#     cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'})
#     memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'})

#     # Update process table
#     processes = []
#     num_cores = psutil.cpu_count()  # Get the number of CPU cores
#     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
#         cpu_usage = proc.info['cpu_percent'] / num_cores  # Normalize CPU usage per core
#         processes.append(html.Tr([
#             html.Td(proc.info['pid']),
#             html.Td(proc.info['name']),
#             html.Td(f"{cpu_usage:.2f}%"),  # Display corrected CPU usage
#             html.Td(f"{proc.info['memory_percent']:.2f}%"),
#             html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0))
#         ]))
    
#     process_table = html.Table([
#         html.Thead(html.Tr([html.Th("PID"), html.Th("Name"), html.Th("CPU (%)"), html.Th("Memory (%)"), html.Th("Action")])),
#         html.Tbody(processes)
#     ])
    
#     return cpu_fig, memory_fig, process_table

# if __name__ == "__main__":
#     app.run(debug=True)










# from dash import Dash, html, dcc, Input, Output, State
# import dash
# import plotly.express as px
# import psutil
# from collections import deque
# import time
# from threading import Thread

# app = Dash(__name__)
# app.title = "Real-Time Process Monitoring Dashboard"

# # Store Data
# cpu_data = deque(maxlen=50)
# memory_data = deque(maxlen=50)
# timestamps = deque(maxlen=50)

# # Layout
# app.layout = html.Div([
#     html.H1("Real-Time Process Monitoring Dashboard", style={
#         "textAlign": "center",
#         "color": "#333",
#         "marginBottom": "20px"
#     }),

#     # Graphs Section
#     html.Div([
#         html.Div(dcc.Graph(id='memory-usage-graph'), style={
#             "flex": "1",
#             "minWidth": "400px",
#             "border": "2px solid #007BFF",
#             "borderRadius": "10px",
#             "padding": "10px",
#             "backgroundColor": "white",
#             "boxShadow": "2px 2px 10px rgba(0,0,0,0.1)"
#         }),
#         html.Div(dcc.Graph(id='cpu-usage-graph'), style={
#             "flex": "1",
#             "minWidth": "400px",
#             "border": "2px solid #28A745",
#             "borderRadius": "10px",
#             "padding": "10px",
#             "backgroundColor": "white",
#             "boxShadow": "2px 2px 10px rgba(0,0,0,0.1)"
#         }),
#     ], style={
#         "display": "flex",
#         "justifyContent": "space-around",
#         "alignItems": "center",
#         "gap": "20px",
#         "marginBottom": "20px"
#     }),

#     # Process Table
#     html.Div(id='process-table', style={
#         "width": "90%",
#         "margin": "auto",
#         "textAlign": "center",
#         "border": "2px solid #ccc",
#         "borderRadius": "10px",
#         "backgroundColor": "white",
#         "boxShadow": "2px 2px 10px rgba(0,0,0,0.1)",
#         "padding": "10px"
#     }),

#     # Auto Update
#     dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
# ], style={"backgroundColor": "#f4f4f4", "padding": "20px"})

# # Data Update Thread
# def update_data():
#     while True:
#         cpu_usage = sum(psutil.cpu_percent(interval=1, percpu=True)) / psutil.cpu_count()  # Multi-core support
#         memory_usage = psutil.virtual_memory().percent
#         timestamps.append(time.strftime("%H:%M:%S"))
#         cpu_data.append(cpu_usage)
#         memory_data.append(memory_usage)
#         time.sleep(2)

# Thread(target=update_data, daemon=True).start()

# # Update Dashboard
# @app.callback(
#     [Output('cpu-usage-graph', 'figure'),
#      Output('memory-usage-graph', 'figure'),
#      Output('process-table', 'children')],
#     [Input('interval-component', 'n_intervals'),
#      Input({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'n_clicks')],
#     [State({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'id')]
# )
# def update_dashboard(n, n_clicks, button_ids):
#     # Handle Process Termination
#     if n_clicks and any(n > 0 for n in n_clicks):
#         for i, clicks in enumerate(n_clicks):
#             if clicks > 0:
#                 pid_to_kill = button_ids[i]['index']
#                 try:
#                     psutil.Process(pid_to_kill).terminate()
#                 except psutil.NoSuchProcess:
#                     pass

#     # CPU & Memory Graphs
#     cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'})
#     memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'})

#     # Process Table
#     processes = []
#     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
#         processes.append(html.Tr([
#             html.Td(proc.info['pid'], style={"padding": "10px", "border": "1px solid #ddd"}),
#             html.Td(proc.info['name'], style={"padding": "10px", "border": "1px solid #ddd"}),
#             html.Td(f"{proc.info['cpu_percent']:.2f}%", style={"padding": "10px", "border": "1px solid #ddd"}),
#             html.Td(f"{proc.info['memory_percent']:.2f}%", style={"padding": "10px", "border": "1px solid #ddd"}),
#             html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0, style={
#                 "backgroundColor": "#FF4136",
#                 "color": "white",
#                 "border": "none",
#                 "padding": "5px 10px",
#                 "cursor": "pointer",
#                 "borderRadius": "5px"
#             }))
#         ]))
    
#     process_table = html.Table([
#         html.Thead(html.Tr([
#             html.Th("PID", style={"padding": "10px", "border": "1px solid #ddd", "backgroundColor": "#007BFF", "color": "white"}),
#             html.Th("Name", style={"padding": "10px", "border": "1px solid #ddd", "backgroundColor": "#007BFF", "color": "white"}),
#             html.Th("CPU (%)", style={"padding": "10px", "border": "1px solid #ddd", "backgroundColor": "#007BFF", "color": "white"}),
#             html.Th("Memory (%)", style={"padding": "10px", "border": "1px solid #ddd", "backgroundColor": "#007BFF", "color": "white"}),
#             html.Th("Action", style={"padding": "10px", "border": "1px solid #ddd", "backgroundColor": "#007BFF", "color": "white"})
#         ])),
#         html.Tbody(processes)
#     ], style={
#         "width": "100%",
#         "margin": "auto",
#         "borderCollapse": "collapse",
#         "borderRadius": "8px",
#         "overflow": "hidden"
#     })

#     return cpu_fig, memory_fig, process_table

# if __name__ == "__main__":
#     app.run(debug=True)










# from dash import Dash, html, dcc, Input, Output
# import dash
# import plotly.express as px
# import psutil
# from collections import deque
# import time
# from threading import Thread

# app = Dash(__name__)
# app.title = "Real-Time Process Monitoring Dashboard"

# # Get number of logical processors
# NUM_CPUS = psutil.cpu_count(logical=True)

# # Data Storage
# cpu_data = deque(maxlen=50)
# memory_data = deque(maxlen=50)
# timestamps = deque(maxlen=50)

# # Layout
# app.layout = html.Div([
#     html.H1("Real-Time Process Monitoring Dashboard", style={"textAlign": "center"}),

#     # Graphs Section
#     html.Div([
#         html.Div([
#             dcc.Graph(id='memory-usage-graph'),
#             html.P(id="memory-text", style={"textAlign": "center", "fontSize": "16px", "fontWeight": "bold"})
#         ], style={"flex": "1", "minWidth": "400px"}),

#         html.Div([
#             dcc.Graph(id='cpu-usage-graph'),
#             html.P(id="cpu-text", style={"textAlign": "center", "fontSize": "16px", "fontWeight": "bold"})
#         ], style={"flex": "1", "minWidth": "400px"}),
#     ], style={"display": "flex", "gap": "20px", "justifyContent": "center"}),

#     # Process Table
#     html.Div(id='process-table', style={"width": "90%", "margin": "auto", "textAlign": "center"}),

#     # Auto Update
#     dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
# ])


# # Data Update Thread
# def update_data():
#     while True:
#         timestamps.append(time.strftime("%H:%M:%S"))
#         cpu_data.append(psutil.cpu_percent())
#         memory_data.append(psutil.virtual_memory().percent)
#         time.sleep(2)


# Thread(target=update_data, daemon=True).start()


# # Update Dashboard
# @app.callback(
#     [Output('cpu-usage-graph', 'figure'),
#      Output('memory-usage-graph', 'figure'),
#      Output('cpu-text', 'children'),
#      Output('memory-text', 'children'),
#      Output('process-table', 'children')],
#     [Input('interval-component', 'n_intervals')]
# )
# def update_dashboard(n):
#     # CPU & Memory Graphs
#     cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'})
#     memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'})

#     # CPU & Memory Usage Text
#     cpu_text = f"CPU Usage: {cpu_data[-1]:.2f}%"
#     memory_text = f"Memory Usage: {memory_data[-1]:.2f}%"

#     # Process Table
#     processes = []
#     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
#         try:
#             # Normalize CPU usage per process
#             cpu_percent = proc.info['cpu_percent'] / NUM_CPUS
#             processes.append(html.Tr([
#                 html.Td(proc.info['pid']),
#                 html.Td(proc.info['name']),
#                 html.Td(f"{cpu_percent:.2f}%"),
#                 html.Td(f"{proc.info['memory_percent']:.2f}%"),
#                 html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0))
#             ]))
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue

#     process_table = html.Table([
#         html.Thead(html.Tr([
#             html.Th("PID"), html.Th("Name"), html.Th("CPU (%)"), html.Th("Memory (%)"), html.Th("Action")
#         ])),
#         html.Tbody(processes)
#     ])

#     return cpu_fig, memory_fig, cpu_text, memory_text, process_table


# if __name__ == "__main__":
#     app.run(debug=True)






# from dash import Dash, html, dcc, Input, Output, State, ctx
# import dash
# import plotly.express as px
# import psutil
# from collections import deque
# import time
# from threading import Thread

# app = Dash(__name__)
# app.title = "Real-Time Process Monitoring Dashboard"

# NUM_CPUS = psutil.cpu_count(logical=True)

# # Data Storage
# cpu_data = deque(maxlen=50)
# memory_data = deque(maxlen=50)
# timestamps = deque(maxlen=50)

# CARD_STYLE = {
#     "backgroundColor": "#1e1e1e",
#     "color": "#ffffff",
#     "borderRadius": "10px",
#     "padding": "15px",
#     "boxShadow": "0px 4px 10px rgba(0,0,0,0.3)",
#     "textAlign": "center"
# }

# app.layout = html.Div([
#     html.H1("Real-Time Process Monitoring Dashboard", style={"textAlign": "center", "color": "#fff"}),

#     html.Div([
#         html.Div([
#             dcc.Graph(id='memory-usage-graph', style={"height": "300px"}),
#             html.P(id="memory-text", style={"textAlign": "center", "fontSize": "16px", "fontWeight": "bold"})
#         ], style={**CARD_STYLE, "flex": "1", "minWidth": "400px"}),

#         html.Div([
#             dcc.Graph(id='cpu-usage-graph', style={"height": "300px"}),
#             html.P(id="cpu-text", style={"textAlign": "center", "fontSize": "16px", "fontWeight": "bold"})
#         ], style={**CARD_STYLE, "flex": "1", "minWidth": "400px"}),
#     ], style={"display": "flex", "gap": "20px", "justifyContent": "center", "margin": "20px"}),

#     html.Div(id='process-table', style={"width": "90%", "margin": "auto", "color": "#fff"}),

#     dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
# ], style={"backgroundColor": "#121212", "padding": "20px", "minHeight": "100vh"})


# # Background Data Collection
# def update_data():
#     while True:
#         timestamps.append(time.strftime("%H:%M:%S"))
#         cpu_data.append(psutil.cpu_percent())
#         memory_data.append(psutil.virtual_memory().percent)
#         time.sleep(2)


# Thread(target=update_data, daemon=True).start()


# # Update Dashboard and Handle Process Killing
# @app.callback(
#     [Output('cpu-usage-graph', 'figure'),
#      Output('memory-usage-graph', 'figure'),
#      Output('cpu-text', 'children'),
#      Output('memory-text', 'children'),
#      Output('process-table', 'children')],
#     [Input('interval-component', 'n_intervals'),
#      Input({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'n_clicks')],
#     [State({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'id')]
# )
# def update_dashboard(n, n_clicks, button_ids):
#     # Handle process termination
#     if n_clicks and any(clicks is not None and clicks > 0 for clicks in n_clicks):
#         for i, clicks in enumerate(n_clicks):
#             if clicks and button_ids:
#                 pid_to_kill = button_ids[i]['index']
#                 try:
#                     psutil.Process(pid_to_kill).terminate()
#                 except (psutil.NoSuchProcess, psutil.AccessDenied):
#                     pass  # Process might have already been killed

#     # Update Graphs
#     cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'})
#     cpu_fig.update_layout(template="plotly_dark")

#     memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'})
#     memory_fig.update_layout(template="plotly_dark")

#     cpu_text = f"CPU Usage: {cpu_data[-1]:.2f}%"
#     memory_text = f"Memory Usage: {memory_data[-1]:.2f}%"

#     # Process Table
#     processes = []
#     for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
#         try:
#             cpu_percent = proc.info['cpu_percent'] / NUM_CPUS
#             processes.append(html.Tr([
#                 html.Td(proc.info['pid'], style={"padding": "8px", "border": "1px solid #666"}),
#                 html.Td(proc.info['name'], style={"padding": "8px", "border": "1px solid #666"}),
#                 html.Td(f"{cpu_percent:.2f}%", style={"padding": "8px", "border": "1px solid #666"}),
#                 html.Td(f"{proc.info['memory_percent']:.2f}%", style={"padding": "8px", "border": "1px solid #666"}),
#                 html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0,
#                                     style={"backgroundColor": "#FF4C4C", "color": "white", "border": "none",
#                                            "padding": "6px 10px", "borderRadius": "5px", "cursor": "pointer"}))
#             ]))
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue

#     process_table = html.Table([
#         html.Thead(html.Tr([
#             html.Th("PID", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
#             html.Th("Name", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
#             html.Th("CPU (%)", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
#             html.Th("Memory (%)", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
#             html.Th("Action", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"})
#         ])),
#         html.Tbody(processes)
#     ], style={"width": "100%", "borderCollapse": "collapse", "marginTop": "20px"})

#     return cpu_fig, memory_fig, cpu_text, memory_text, process_table


# if __name__ == "__main__":
#     app.run(debug=True)







from dash import Dash, html, dcc, Input, Output, State, ctx
import dash
import plotly.express as px
import psutil
from collections import deque
import time
from threading import Thread

app = Dash(__name__)
app.title = "Real-Time Process Monitoring Dashboard"

NUM_CPUS = psutil.cpu_count(logical=True)

# Data Storage (Keep only last 10 seconds of data)
cpu_data = deque(maxlen=5)  # 5 entries, since interval is 2 sec -> 10 sec data
memory_data = deque(maxlen=5)
timestamps = deque(maxlen=5)

CARD_STYLE = {
    "backgroundColor": "#1e1e1e",
    "color": "#ffffff",
    "borderRadius": "10px",
    "padding": "15px",
    "boxShadow": "0px 4px 10px rgba(0,0,0,0.3)",
    "textAlign": "center"
}

app.layout = html.Div([
    html.H1("Real-Time Process Monitoring Dashboard", style={"textAlign": "center", "color": "#fff"}),

    html.Div([
        html.Div([
            dcc.Graph(id='memory-usage-graph', style={"height": "300px"}),
            html.P(id="memory-text", style={"textAlign": "center", "fontSize": "16px", "fontWeight": "bold"})
        ], style={**CARD_STYLE, "flex": "1", "minWidth": "400px"}),

        html.Div([
            dcc.Graph(id='cpu-usage-graph', style={"height": "300px"}),
            html.P(id="cpu-text", style={"textAlign": "center", "fontSize": "16px", "fontWeight": "bold"})
        ], style={**CARD_STYLE, "flex": "1", "minWidth": "400px"}),
    ], style={"display": "flex", "gap": "20px", "justifyContent": "center", "margin": "20px"}),

    html.Div(id='process-table', style={"width": "90%", "margin": "auto", "color": "#fff"}),

    dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
], style={"backgroundColor": "#121212", "padding": "20px", "minHeight": "100vh"})


# Background Data Collection
def update_data():
    while True:
        timestamps.append(time.strftime("%H:%M:%S"))
        cpu_data.append(psutil.cpu_percent())
        memory_data.append(psutil.virtual_memory().percent)
        time.sleep(2)

Thread(target=update_data, daemon=True).start()


# Update Dashboard and Handle Process Killing
@app.callback(
    [Output('cpu-usage-graph', 'figure'),
     Output('memory-usage-graph', 'figure'),
     Output('cpu-text', 'children'),
     Output('memory-text', 'children'),
     Output('process-table', 'children')],
    [Input('interval-component', 'n_intervals'),
     Input({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'n_clicks')],
    [State({'type': 'kill-btn', 'index': dash.dependencies.ALL}, 'id')]
)
def update_dashboard(n, n_clicks, button_ids):
    # Handle process termination
    if n_clicks and any(clicks is not None and clicks > 0 for clicks in n_clicks):
        for i, clicks in enumerate(n_clicks):
            if clicks and button_ids:
                pid_to_kill = button_ids[i]['index']
                try:
                    psutil.Process(pid_to_kill).terminate()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass  # Process might have already been killed

    # Update Graphs
    cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'})
    cpu_fig.update_layout(template="plotly_dark")

    memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'})
    memory_fig.update_layout(template="plotly_dark")

    cpu_text = f"CPU Usage: {cpu_data[-1]:.2f}%"
    memory_text = f"Memory Usage: {memory_data[-1]:.2f}%"

    # Process Table
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            cpu_percent = proc.info['cpu_percent'] / NUM_CPUS
            processes.append(html.Tr([
                html.Td(proc.info['pid'], style={"padding": "8px", "border": "1px solid #666"}),
                html.Td(proc.info['name'], style={"padding": "8px", "border": "1px solid #666"}),
                html.Td(f"{cpu_percent:.2f}%", style={"padding": "8px", "border": "1px solid #666"}),
                html.Td(f"{proc.info['memory_percent']:.2f}%", style={"padding": "8px", "border": "1px solid #666"}),
                html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0,
                                    style={"backgroundColor": "#FF4C4C", "color": "white", "border": "none",
                                           "padding": "6px 10px", "borderRadius": "5px", "cursor": "pointer"}))
            ]))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    process_table = html.Table([
        html.Thead(html.Tr([
            html.Th("PID", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
            html.Th("Name", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
            html.Th("CPU (%)", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
            html.Th("Memory (%)", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"}),
            html.Th("Action", style={"padding": "10px", "border": "1px solid #888", "backgroundColor": "#333"})
        ])),
        html.Tbody(processes)
    ], style={"width": "100%", "borderCollapse": "collapse", "marginTop": "20px"})

    return cpu_fig, memory_fig, cpu_text, memory_text, process_table


if __name__ == "__main__":
    app.run(debug=True)



