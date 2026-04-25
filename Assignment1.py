import tkinter
import tkinter.messagebox

class StreamMasterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('StreamMaster Cost Estimator')
        self.main_window.configure(bg='#f8fbff')

        section_font = ('Arial', 12, 'bold')
        label_font = ('Arial', 10)

        # Subscription Tier (Radio Buttons)
        self.subscription_lbframe = tkinter.LabelFrame(self.main_window, text='Subscription Tier', bg='#f8fbff', font=section_font
                                                       ,labelanchor='n')
        self.subscription_lbframe.pack(padx=20, pady=10, fill='x')
        
        self.tier_var = tkinter.IntVar()
        self.tier_var.set(20)

        self.basic_rb = tkinter.Radiobutton(self.subscription_lbframe, text= 'Basic (RM20/profile)', bg='#f8fbff',
                                            variable= self.tier_var, value= 20)
        self.standard_rb = tkinter.Radiobutton(self.subscription_lbframe, text= 'Standard (RM30/profile)', bg='#f8fbff',
                                               variable= self.tier_var, value= 30)
        self.premium_rb = tkinter.Radiobutton(self.subscription_lbframe, text='Premium (RM45/profile)', bg='#f8fbff',
                                              variable= self.tier_var, value= 45)

        self.basic_rb.pack(anchor='w', padx=10)
        self.standard_rb.pack(anchor='w', padx=10)
        self.premium_rb.pack(anchor='w', padx=10)

        # Number of Profiles (Entry)
        self.profile_lbframe = tkinter.LabelFrame(self.main_window, text='Profiles', bg='#f8fbff', font=section_font,
                                                  labelanchor='n')
        self.profile_lbframe.pack(padx=20, pady=10, fill='x')
        
        self.profile_label = tkinter.Label(self.profile_lbframe, text='Enter number of profile:', bg='#f8fbff', font=label_font)
        self.profile_label.pack(side='left', padx=10, pady = 5)
        self.profile_entry = tkinter.Entry(self.profile_lbframe)
        self.profile_entry.pack(side='left', padx=10, pady = 5)

        # Add-ons (Checkbox)
        self.addon_lbframe = tkinter.LabelFrame(self.main_window, text='Add-on Services', bg='#f8fbff', font=section_font,
                                                labelanchor='n')
        self.addon_lbframe.pack(padx=20, pady=10, fill='x')        

        self.fourK_var = tkinter.BooleanVar()
        self.offline_var = tkinter.BooleanVar()
        self.extra_var = tkinter.BooleanVar()

        self.fourK_cb = tkinter.Checkbutton(self.addon_lbframe, text= '4K Streaming (RM10)', bg='#f8fbff',
                                            variable= self.fourK_var)
        self.offline_cb = tkinter.Checkbutton(self.addon_lbframe, text= 'Offline Downloads (RM5)', bg='#f8fbff',
                                              variable= self.offline_var)
        self.extra_cb = tkinter.Checkbutton(self.addon_lbframe, text= 'Extra Device Login (RM7)', bg='#f8fbff',
                                            variable= self.extra_var)

        self.fourK_cb.pack(anchor='w', padx=10)
        self.offline_cb.pack(anchor='w', padx=10)
        self.extra_cb.pack(anchor='w', padx=10)

        # Tax Rate (Entry)
        self.tax_lbframe = tkinter.LabelFrame(self.main_window, text='Tax', bg='#f8fbff', font=section_font,
                                              labelanchor='n')
        self.tax_lbframe.pack(padx=20, pady=10, fill='x')
        
        self.tax_label = tkinter.Label(self.tax_lbframe, text='Enter tax rate (in %):', bg='#f8fbff', font=label_font)
        self.tax_label.pack(side='left', padx=19, pady = 5)
        self.tax_entry = tkinter.Entry(self.tax_lbframe)
        self.tax_entry.pack(side='left', padx=10, pady = 5)

        # Buttons
        self.bottom_frame = tkinter.Frame(self.main_window, bg='#f8fbff')
        self.bottom_frame.pack(anchor='center', pady=13)
        
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Calculate', bg='#cdefff', font=label_font, width=10,
                                          command= self.displayTotal)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', bg='#ffc0c0', font=label_font, width=10,
                                          command=self.main_window.destroy)

        self.calc_button.pack(side='left', padx=10)
        self.quit_button.pack(side='left', padx=10)

        # main loop
        tkinter.mainloop()
        
    def displayTotal(self):
        addOn = 0
        if ((int(self.profile_entry.get()) <= 0) or (float(self.tax_entry.get()) < 0)):
            tkinter.messagebox.showinfo('Invalid Input', 'Please enter number larger than 0 only in Number of Profile and Tax Rate.')
        else:
            # Calculation of cost
            if (self.fourK_var.get()):
                addOn += 10
            if (self.offline_var.get()):
                addOn += 5
            if (self.extra_var.get()):
                addOn += 7           

            basePrice = int(self.tier_var.get())
            profile = int(self.profile_entry.get())
            tax = float(self.tax_entry.get())

            total = ((basePrice * profile) + addOn) * (1 + (tax/100))
            if (total >= 500):
                tkinter.messagebox.showwarning('Warning', 'Total cost exceeds RM500')

            # Format 2 dcp
            baseCost = round(basePrice * profile, 2)
            addonCost = round(addOn, 2)
            taxCost = round(((basePrice * profile) + addOn) * (tax/100),2)
            finalCost = round(total, 2)

            # SUmmary Report Window
            summary_window = tkinter.Toplevel(self.main_window)
            summary_window.title('Estimated Monthly Cost')
            summary_window.configure(bg='#ffffff')

            summary_lbframe = tkinter.LabelFrame(summary_window, text='Summary Report', bg='#ffffff',
                                     font=('Arial', 12, 'bold'), labelanchor='n')
            summary_lbframe.pack(padx=20, pady=20, fill='x')

            summaryText = ('Base cost:                      RM' + format(baseCost, '.2f') +
                            '\nSelected add-on costs:     RM' + format(addonCost, '.2f') +
                            '\nApplied taxes:                  RM' + format(addonCost, '.2f') +
                            '\n===========================================' +
                            '\nFinal total:                        RM' + format(finalCost, '.2f'))

            summary_label = tkinter.Label(summary_lbframe, text= summaryText, bg='#ffffff', font=('Arial', 10), justify='left')
            summary_label.pack(anchor='w', padx=20, pady = 10)                       
        

# Create the GUI
mygui = StreamMasterGUI()
