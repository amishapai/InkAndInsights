import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window to full screen
        self.attributes('-fullscreen', True)

        # Configure the window
        self.title("INK AND INSIGHTS")
        self.configure(background='white')

        # Heading label
        heading_label = ttk.Label(self, text='INK AND INSIGHTS', font=('Times New Roman', 50), foreground="#1B8E91")
        heading_label.configure(style='Main.TLabel')  # Set background color using style
        heading_label.pack(pady=10)

        # Subheading label
        subheading_label = ttk.Label(self, text='(NAVIGATING INDIA’S LITERACY METRICS)', font=('Arial', 20), foreground='blue')
        subheading_label.configure(style='Main.TLabel')  # Set background color using style
        subheading_label.pack(pady=10)

        # Buttons container
        buttons_container = ttk.Frame(self)
        buttons_container.pack(pady=10)

        # Button 1
        button1 = ttk.Button(buttons_container, text='Basic Insights', command=self.open_window1)
        button1.grid(row=0, column=0, padx=20, pady=10, ipadx=50, ipady=50)

        # Button 2
        button2 = ttk.Button(buttons_container, text='Amenities-Literacy Correlation', command=self.open_window2)
        button2.grid(row=0, column=1, padx=20, pady=10,ipadx=50, ipady=50 )

        # Button 3
        button3 = ttk.Button(buttons_container, text='ML Models',  command=self.open_window3)
        button3.grid(row=0, column=2, padx=20, pady=10,ipadx=50, ipady=50 )

        # Load images
        image1 = PhotoImage(file="C:\\Users\\amish\\Python\\InkAndInsights\\Images\\Main-1.png")
        image2 = PhotoImage(file="C:\\Users\\amish\\Python\\InkAndInsights\\Images\\Main-2.png")

        # Images
        image_label1 = ttk.Label(self, image=image1)
        image_label1.configure(style='Main.TLabel')  # Set background color using style
        image_label1.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        image_label2 = ttk.Label(self, image=image2)
        image_label2.configure(style='Main.TLabel')  # Set background color using style
        image_label2.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        self.image_references = [image1, image2]

        # Create a style to set the background color
        style = ttk.Style(self)
        style.configure('Main.TLabel', background='white')
        # Bind the Escape key to exit full screen
        self.bind("<Escape>", self.exit_full_screen)
    def open_window1(self):
        window_one = WindowOne(self)
    def exit_full_screen(self, event):
        # Exit full screen when the Escape key is pressed
        self.attributes('-fullscreen', False)
    def open_window2(self):
        window_two = WindowTwo(self)

    def open_window3(self):
        window_three = WindowThree(self)

class WindowOne(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()


        # Configure the window
        self.title("INK AND INSIGHTS")
        self.configure(background='white')

        # Heading label
        heading_label = tk.Label(self, text='INK AND INSIGHTS', font=('Times New Roman', 50), foreground="#1B8E91")
        heading_label.pack(pady=10)

        # Subheading label
        subheading_label = tk.Label(self, text='(NAVIGATING INDIA’S LITERACY METRICS)', font=('Arial', 20), foreground='blue')
        subheading_label.pack(pady=10)

        # Buttons container
        buttons_container = tk.Frame(self)
        buttons_container.pack(pady=10)

        # Button 1
        button1 = tk.Button(buttons_container, text='Schools Data', command=self.function1)
        button1.grid(row=0, column=0, padx=20, pady=10, ipadx=50, ipady=50)

        # Button 2
        button2 = tk.Button(buttons_container, text='Gender Ratio & Female Literacy', command=self.function2)
        button2.grid(row=0, column=1, padx=20, pady=10, ipadx=50, ipady=50)

        # Button 3
        button3 = tk.Button(buttons_container, text='HeatMap DistrictWise', command=self.function3)
        button3.grid(row=1, column=0, padx=20, pady=10, ipadx=50, ipady=50)

        # Button 4
        button4 = tk.Button(buttons_container, text='Male Vs. Female Literacy', command=self.function4)
        button4.grid(row=1, column=1, padx=20, pady=10, ipadx=50, ipady=50)

    def function1(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        filePath = "C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv"
        data = pd.read_csv(filePath)
        x_column = "STATNAME"  
        y_column = "SCHTOT"  
        x_data = data[x_column]
        y_data = data[y_column]
        plt.bar(x_data, y_data)
        plt.xlabel("States")
        plt.ylabel("Total Schools")
        plt.xticks(rotation=90)
        plt.show()

    def function2(self):
        import matplotlib.pyplot as plt
        import pandas as pd

        # Step 1: Read the CSV file into a DataFrame
        df = pd.read_csv("C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv")
        x_column= "STATNAME"
        y_column= "SEXRATIO"
        y_column1='FEMALE_LIT'
        x_df= df[x_column]
        y_df= (df[y_column]/1000)*100
        y_df1= df[y_column1]
        plt.scatter(x_df, y_df, label = 'Gender Ratio', color = 'blue')
        plt.scatter(x_df, y_df1, label ='Female Literacy', color= 'brown')
        plt.legend()
        plt.xlabel("States")
        plt.ylabel("Gender Ratio and Female Literacy")
        plt.xticks(range(len(x_df)), x_df, rotation='vertical')
        plt.show()

    def function3(self):
        import matplotlib.pyplot as plt
        import pandas as pd
        import seaborn as sns 
        df = pd.read_csv("C:\\Users\\amish\\Downloads\\HMP.csv")
        dfHeatMap= df.pivot_table(index="STATNAME",columns='DISTCD', values='LIT', aggfunc='mean', fill_value=0)
        ax = plt.axes()
        sns.heatmap(data=dfHeatMap, annot=True, ax = ax)
        ax.set_title('Literacy rate- state and districtwise')
        plt.show()

    def function4(self):
        import pandas as pd
        import matplotlib.pyplot as plt

        file_path = 'C:\\Users\\amish\\Downloads\\python_el_2.csv'  
        data = pd.read_csv(file_path)

        x_column = 'STATNAME'  
        y1_column = 'MALE_LIT'  
        y2_column = 'FEMALE_LIT'  

        x_data = data[x_column]
        y1_data = data[y1_column]
        y2_data = data[y2_column]

        plt.plot(x_data, y1_data, label = "Male literacy",linewidth=3.5)
        plt.plot(x_data, y2_data, label = "Female literacy",linewidth=3.5, color='green')
        plt.xticks(range(len(x_data)), x_data, rotation='vertical')
        plt.xlabel('States')
        plt.ylabel('Literacy rate')
        plt.legend()
        plt.grid(True)
        plt.title("MALE VS FEMALE LITERACY RATE")
        plt.show()


class WindowTwo(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

# Configure the window
        self.title("INK AND INSIGHTS")
        self.configure(background='white')

        # Heading label
        heading_label = tk.Label(self, text='INK AND INSIGHTS', font=('Times New Roman', 50), foreground="#1B8E91")
        heading_label.pack(pady=10)

        # Subheading label
        subheading_label = tk.Label(self, text='(NAVIGATING INDIA’S LITERACY METRICS)', font=('Arial', 20), foreground='blue')
        subheading_label.pack(pady=10)

        # Buttons container
        buttons_container = tk.Frame(self)
        buttons_container.pack(pady=10)

        # Button 1
        button1 = ttk.Button(buttons_container, text='Educational Facilities by State', command=self.button1_action)
        button1.grid(row=0, column=0, padx=20, pady=10, ipadx=50, ipady=50)

        # Button 2
        button2 = ttk.Button(buttons_container, text='Impact of Amenities on Literacy', command=self.button2_action)
        button2.grid(row=0, column=1, padx=20, pady=10,ipadx=50, ipady=50 )

        # Button 3
        button3 = ttk.Button(buttons_container, text='Dual Variable Impact- 3D Modeling',  command=self.button3_action)
        button3.grid(row=0, column=2, padx=20, pady=10,ipadx=50, ipady=50 )

    def button1_action(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np
        file_path= "C:\\Users\\amish\\Downloads\\python_el_1.csv"
        df=pd.read_csv(file_path)
        df1 = pd.read_csv("C:\\Users\\amish\\Python\\InkandInsights\\2015_16_Statewise_Elementary.csv")
        x_column= "STATNAME"
        y_column1= "KITSTOT"
        y_column= "SCHTOT"
        x_df= df[x_column]
        y_df= df[y_column]
        y_df1= df1[y_column1]
        plt.bar(x_df, y_df, label = "Number of schools", color='#900C3F')
        plt.bar(x_df, y_df1, label = "Number of schools- midday meals", color='black')
        plt.xlabel("States")
        plt.ylabel("Number of Schools and those providing midday meals")
        plt.xticks(range(len(x_df)), x_df, rotation='vertical')
        plt.grid(axis='y')
        plt.legend()
        plt.show()

        filePath= "C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv"
        data = pd.read_csv(filePath)
        data1 = pd.read_csv(filePath)

        x_column = "STATNAME"
        y_column1 = "SGTOILTOT"
        y_column = "SCHTOT"

        x_data = data[x_column]
        y_data = data1[y_column]
        y_data1 = data1[y_column1]

        plt.bar(x_data, y_data, label = "Number of schools", color = "maroon")
        plt.bar(x_data, y_data1, label = "Number of schools with girls toilet", color = "orange")

        plt.xlabel("States")
        plt.ylabel("Number of Schools and those with girls toilet")
        plt.xticks(range(len(x_data)), x_data, rotation=90)
        plt.grid(axis='y')

        plt.legend()
        plt.show()

        filePath= "C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv"
        data = pd.read_csv(filePath)
        data1 = pd.read_csv(filePath)

        x_column = "STATNAME"
        y_column1 = "SELETOT"
        y_column = "SCHTOT"

        x_data = data[x_column]
        y_data = data1[y_column]
        y_data1 = data1[y_column1]

        plt.bar(x_data, y_data, label = "Number of schools", color = "black")
        plt.bar(x_data, y_data1, label = "Number of schools: electricity", color = "purple")

        plt.xlabel("States")
        plt.ylabel("Number of Schools and those with electricity")
        plt.xticks(range(len(x_data)), x_data, rotation=90)
        plt.grid(axis='y')

        plt.legend()
        plt.show()

        filePath= "C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv"
        data = pd.read_csv(filePath)
        data1 = pd.read_csv(filePath)

        x_column = "STATNAME"
        y_column1 = "ROADTOT"
        y_column = "SCHTOT"

        x_data = data[x_column]
        y_data = data1[y_column]
        y_data1 = data1[y_column1]

        plt.bar(x_data, y_data, label = "Number of schools", color = "black")
        plt.bar(x_data, y_data1, label = "Number of schools: approachable by road", color = "pink")

        plt.xlabel("States")
        plt.ylabel("Number of Schools and those appraochable by all weather road")
        plt.xticks(range(len(x_data)), x_data, rotation=90)
        plt.grid(axis='y')

        plt.legend()
        plt.show()

    def button2_action(self):
        import pandas as pd
        import matplotlib.pyplot as plt

        file_path =  "C:\\Users\\amish\\Python\\InkAndInsights\\csv3.csv"   
        data = pd.read_csv(file_path)


        x_column = 'statname'  
        y1_column = '%girls_toilet'  
        y2_column = 'female_literacy_rate'  


        x_data = data[x_column]
        y1_data = data[y1_column]
        y2_data = data[y2_column]

        plt.scatter(x_data, y1_data, color='olive', label="% schools with girls toilet")
        plt.bar(x_data, y2_data, color='peru', label ="Female literacy rate")

        plt.xlabel('States')
        plt.ylabel('Dependency of female literacy rate on girls washroom')
        plt.legend(loc='best')
        plt.xticks(rotation=90)
        plt.show()

        
        file_path = "C:\\Users\\amish\\Python\\InkAndInsights\\csv3.csv" 
        data = pd.read_csv(file_path)


        x_column = 'statname'  
        y1_column = '%mdm'  
        y2_column = 'OVERALL_LI'  


        x_data = data[x_column]
        y1_data = data[y1_column]
        y2_data = data[y2_column]

        plt.plot(x_data, y1_data, color='black', label='%schools with midday meals')
        plt.bar(x_data, y2_data, color='pink', label ='Overall Literacy rate')
        plt.xticks(rotation=90)

        plt.xlabel('States')
        plt.ylabel('Dependency of literacy rate on schools with midday meals ')
        plt.legend()

        plt.show()
        
        file_path = "C:\\Users\\amish\\Python\\InkAndInsights\\csv3.csv"  
        data = pd.read_csv(file_path)


        x_column = 'statname'  
        y1_column = '%road'  
        y2_column = 'OVERALL_LI'  


        x_data = data[x_column]
        y1_data = data[y1_column]
        y2_data = data[y2_column]

        plt.scatter(x_data, y1_data, color='orange', label="% schools with road access")
        plt.scatter(x_data, y2_data, color='blue', label ="Overall Literacy Rate")

        plt.xlabel('States')
        plt.ylabel('Dependency of literacy rate on schools with road access')
        plt.legend()
        plt.xticks(rotation=90)
        plt.show()
        file_path = "C:\\Users\\amish\\Python\\InkAndInsights\\csv3.csv"  
        data = pd.read_csv(file_path)


        x_column = 'statname'  
        y1_column = '%electric_all'  
        y2_column = 'OVERALL_LI'  


        x_data = data[x_column]
        y1_data = data[y1_column]
        y2_data = data[y2_column]

        plt.plot(x_data, y1_data, color='red', label="% schools with electricity")
        plt.plot(x_data, y2_data, color='black', label = "Overall Literacy Rate")

        plt.xlabel('States')
        plt.ylabel('Dependency of schools with electricity on literacy rate')
        plt.legend()
        plt.xticks(rotation=90)
        plt.show()
    def button3_action(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        file_path = "C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv"
        data = pd.read_csv(file_path)


        label = 'STATNAME'  
        x = 'MALE_LIT'  
        y = 'FEMALE_LIT'  
        z = 'OVERALL_LI'
        l=data[label]
        x_data = data[x]
        y1_data = data[y]
        y2_data = data[z]

        # Create a 3D bar plot
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection='3d')

        # Plot the 3D bars
        x_values = range(len(l))
        y_values = x_data
        z_values = [1] * len(l)
        ax.bar(x_values, y_values, z_values, color='blue', alpha=0.7, label='Male_Lit')

        y_values = y1_data
        z_values = [2] * len(l)
        ax.bar(x_values, y_values, z_values, color='pink', alpha=0.7, label='Female_Lit')

        y_values = y2_data
        z_values = [3] * len(l)
        ax.bar(x_values, y_values, z_values, color='green', alpha=0.7, label='Overall_Lit')

        # Set labels and title
        ax.set_xticks(x_values)
        ax.set_xticklabels(l, rotation=90)

        ax.set_ylabel('Literacy rate')
        ax.set_zlabel('Category')
        ax.set_title('3D Bar Plot of Literacy Rates')

        # Add legend
        ax.legend()
        plt.show()
        file_path = "C:\\Users\\amish\\Python\\InkAndInsights\\csv3.csv"  
        data = pd.read_csv(file_path)

        y1_column = 'female_literacy_rate'  
        y2_column = '%girls_toilet'  

        y = data[y1_column]
        z = data[y2_column]

        # Create a 3D scatter plot
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection='3d')

        # Scatter plot using the index as x-axis
        scatter = ax.scatter(data.index, y, z, c='blue', marker='o')

        # Set labels and title
        ax.set_ylabel('% Female Literacy')
        ax.set_zlabel('% Girls in Schools')
        ax.set_title('3D Scatter Plot: Index vs % Female Literacy vs % Girls in Schools')

        # Set state names as labels on the x-axis
        ax.set_xticks(data.index)
        ax.set_xticklabels(data['statname'], rotation=90)

        # Show plot
        plt.show()

class WindowThree(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()


        # Configure the window
        self.title("INK AND INSIGHTS")
        self.configure(background='white')

        # Heading label
        heading_label = tk.Label(self, text='INK AND INSIGHTS', font=('Times New Roman', 50), foreground="#1B8E91")
        heading_label.pack(pady=10)

        # Subheading label
        subheading_label = tk.Label(self, text='(NAVIGATING INDIA’S LITERACY METRICS)', font=('Arial', 20), foreground='blue')
        subheading_label.pack(pady=10)

        # Buttons container
        buttons_container = tk.Frame(self)
        buttons_container.pack(pady=10)

        # Button 1
        button1 = tk.Button(buttons_container, text='K-Means CLustering', command=self.func1)
        button1.grid(row=0, column=0, padx=20, pady=10, ipadx=50, ipady=50)

        # Button 2
        button2 = tk.Button(buttons_container, text='Linear Regression', command=self.func2)
        button2.grid(row=0, column=1, padx=20, pady=10, ipadx=50, ipady=50)

    def func1(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler

        # Load the dataset
        file_path = 'C:\\Users\\amish\\Downloads\\python_el_2.csv'  
        data = pd.read_csv(file_path)

        # Extract male and female literacy rate columns
        x_column = 'STATNAME'  
        y1_column = 'MALE_LIT'  
        y2_column = 'FEMALE_LIT'  

        x_data = data[x_column]
        y1_data = data[y1_column].values.reshape(-1, 1)  # Reshape to make it a column vector
        y2_data = data[y2_column].values.reshape(-1, 1)  # Reshape to make it a column vector

        # Standardize the data
        scaler = StandardScaler()
        y1_scaled = scaler.fit_transform(y1_data)
        y2_scaled = scaler.fit_transform(y2_data)

        # Perform K-means clustering for male literacy
        kmeans_male = KMeans(n_clusters=3, random_state=42)
        data['Male_Cluster'] = kmeans_male.fit_predict(y1_scaled)

        # Perform K-means clustering for female literacy
        kmeans_female = KMeans(n_clusters=3, random_state=42)
        data['Female_Cluster'] = kmeans_female.fit_predict(y2_scaled)

        # Visualize the results
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # Plot Male Literacy Rate
        ax1.scatter(x_data, y1_data, c=data['Male_Cluster'], cmap='viridis')
        ax1.set_ylabel('Male Literacy Rate')
        ax1.set_title('K-means Clustering for Male Literacy Rate')

        # Plot Female Literacy Rate
        ax2.scatter(x_data, y2_data, c=data['Female_Cluster'], cmap='viridis')
        ax2.set_xlabel('States')
        ax2.set_ylabel('Female Literacy Rate')
        ax2.set_title('K-means Clustering for Female Literacy Rate')

        plt.xticks(rotation='vertical')
        plt.show()


    def func2(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        from sklearn.linear_model import LinearRegression
        import numpy as np
        file_path = "C:\\Users\\amish\\Python\\InkAndInsights\\csv3.csv"
        data = pd.read_csv(file_path)

        # Step 2: Select relevant columns
        x_column = 'statname'
        y1_column = '%girls_toilet'
        y2_column = 'female_literacy_rate'

        x_data = data[x_column]
        y1_data = data[y1_column]
        y2_data = data[y2_column]

        # Step 3: Reshape the data
        X = y1_data.values.reshape(-1, 1)  # Independent variable
        y = y2_data.values.reshape(-1, 1)  # Dependent variable

        # Step 4: Create and fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Step 5: Make predictions
        y_pred = model.predict(X)

        # Step 6: Visualize the results
        plt.scatter(X, y, color='olive', label="% Schools with Girls Toilet")
        plt.plot(X, y_pred, color='red', label='Linear Regression', linewidth=2)
        plt.xlabel('% Schools with Girls Toilet')
        plt.ylabel('Female Literacy Rate')
        plt.legend(loc='best')
        plt.title('Linear Regression: Female Literacy Rate vs % Schools with Girls Toilet')
        plt.show()
if __name__ == "__main__":
    app = MainPage()
    app.mainloop()

