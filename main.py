from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
  def __init__(self,root):
    self.root=root
    self.root.title("Hospital Management System")
    self.root.geometry("1540x800+0+0")

    self.NameOftablet=StringVar()
    self.ref=StringVar()
    self.Dose = StringVar()
    self.NumberofTablet = StringVar()
    self.Lot = StringVar()
    self.Issuedate = StringVar()
    self.ExpDate = StringVar()
    self.DailyDose = StringVar()
    self.sideEfect = StringVar()
    self.FurtherInformation = StringVar()
    self.StorageAdvice = StringVar()
    self.DrivingUsingMachine = StringVar()
    self.HowtoUseMedication = StringVar()
    self.PatientId = StringVar()
    self.nhsNumber = StringVar()
    self.PatientName = StringVar()
    self.DateOfBirth = StringVar()
    self.PatientAddress = StringVar()


    lbltitle=Label(self.root, bd=20, relief=RIDGE, text="+ Hospital Management System", fg="red", bg="white", font=("times new roman", 50,"bold"))
    lbltitle.pack(side=TOP, fill=X)


    
    DataFrame=Frame(self.root,bd=20,relief=RIDGE)
    DataFrame.place(x=0,y=130,width=1440,height=400)

    DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                               font=("times new roman", 12, "bold"), text="Patient Information")
    DataFrameLeft.place(x=0, y=5, width=950, height=350)

    DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                font=("times new roman", 12, "bold"), text="Prescription")
    DataFrameRight.place(x=960, y=5, width=430, height=350)



    Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
    Buttonframe.place(x=0, y=530, width=1440, height=70)


    Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
    Detailsframe.place(x=0, y=600, width=1440, height=200)


    lblNameTablet=Label(DataFrameLeft,
                        text="Names of Tablet", font=("times new roman", 12,"bold"), padx=2, pady=6)
    lblNameTablet.grid(row=0,column=0,sticky=W)

    comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameOftablet,state="readonly",font=("times new roman", 12, "bold"),
                                                                            width=40)
    comNameTablet["values"]= ("Nice","Corona Vaccine","Acetaminophen","Adderall", "Amlodipine","Ativan")
    comNameTablet.current(0)
    comNameTablet.grid(row=0,column=1)

    lblref = Label(DataFrameLeft, font=("arial", 12,"bold"), text="Refernce No:", padx=2)
    lblref.grid(row=1,column=0,sticky=W)
    txtref=Entry(DataFrameLeft,font=("arial", 13,"bold"),textvariable=self.ref, width=33)
    txtref.grid(row=1,column=1)

    lblDoes = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose: ", padx=2)
    lblDoes.grid(row=2, column=0, sticky=W)
    txtDoes = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.Dose, width=33)
    txtDoes.grid(row=2, column=1)

    lblNTable = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2)
    lblNTable.grid(row=3, column=0, sticky=W)
    txtNTable= Entry(DataFrameLeft, font=("arial",13,"bold"), textvariable=self.NumberofTablet,width=33)
    txtNTable.grid(row=3, column=1)

    lblLot = Label(DataFrameLeft, font=("arial",12,"bold"), text="Lot:",padx=2 )
    lblLot.grid(row=4, column=0, sticky=W)
    txtLot = Entry(DataFrameLeft, font=("arial",13,"bold"), textvariable=self.Lot,width=33)
    txtLot.grid(row=4, column=1)

    lblIsDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2)
    lblIsDate.grid(row=5, column=0, sticky=W)
    txtIsDate= Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable=self.Issuedate, width=33)
    txtIsDate.grid(row=5,column=1)

    lblExpDate= Label(DataFrameLeft, font=("arial", 12,"bold"), text="Exp Date:", padx=2)
    lblExpDate.grid(row=6, column=0, sticky=W)
    txtExDate = Entry(DataFrameLeft, font=("arial",13,"bold"), textvariable=self.ExpDate,width=33)
    txtExDate.grid(row=6, column=1)

    lblDlyDose =Label(DataFrameLeft, font=("arial",12,"bold"),text="Daily Dose:",padx=2)
    lblDlyDose.grid(row=7,column=0,sticky=W)
    txtDlyDose=Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable=self.DailyDose,width=33)
    txtDlyDose.grid(row=7,column=1)

    lblSdEffect = Label(DataFrameLeft, font=("arial",12,"bold"),text="Side Effect:",padx=2)
    lblSdEffect.grid(row=8,column=0,sticky=W)
    txtSdEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=33)
    txtSdEffect.grid(row=8,column=1)

    lblFurInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information: ", padx=2)
    lblFurInfo.grid(row=0,column=2,sticky=W)
    txtFurInfo=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=33)
    txtFurInfo.grid(row=0,column=3)

    lblDrivingUsingMachine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2)
    lblDrivingUsingMachine.grid(row=1,column=2,sticky=W)
    txtDrivingUsingMachine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=33)
    txtDrivingUsingMachine.grid(row=1,column=3)

    lblStoAdvice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2)
    lblStoAdvice.grid(row=2,column=2,sticky=W)
    txtStoAdvice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=33)
    txtStoAdvice.grid(row=2,column=3)

    lblMedication=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication: ", padx=2)
    lblMedication.grid(row=3,column=2,sticky=W)
    txtMedication=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.HowtoUseMedication,width=33)
    txtMedication.grid(row=3,column=3)

    lblPatientId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id: ", padx=2)
    lblPatientId.grid(row=4, column=2, sticky=W)
    txtPatientId = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.PatientId,width=33)
    txtPatientId.grid(row=4, column=3)

    lblNHSNum = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number: ", padx=2)
    lblNHSNum.grid(row=5, column=2, sticky=W)
    txtNHSNum = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.nhsNumber,width=33)
    txtNHSNum.grid(row=5, column=3)

    lblPatientName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name: ", padx=2)
    lblPatientName.grid(row=6, column=2, sticky=W)
    txtPatientName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.PatientName, width=33)
    txtPatientName.grid(row=6, column=3)

    lblDOB = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth: ", padx=2)
    lblDOB.grid(row=7, column=2, sticky=W)
    txtDOB = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.DateOfBirth,width=33)
    txtDOB.grid(row=7, column=3)

    lblPatientAdd = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address: ", padx=2)
    lblPatientAdd.grid(row=8, column=2, sticky=W)
    txtPatientAdd = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.PatientAddress,width=33)
    txtPatientAdd.grid(row=8, column=3)


    self.txtPrescription=Text(DataFrameRight, font=("arial",12,"bold"),width=50,height=20,padx=2,pady=6)
    self.txtPrescription.grid(row=0,column=0)


    btnPrescription = Button(Buttonframe, command=self.iPrectioption,text="Prescription", bg="gray", fg="blue", font=("arial", 12, "bold"),
                             width=32, height=2, padx=2, pady=6)
    btnPrescription.grid(row=0, column=0)

    btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="white", fg="blue", font=("arial", 12, "bold"),
                             width=32, height=2, padx=2, pady=6)
    btnPrescriptionData.grid(row=0, column=1)

    btnUpdate=Button(Buttonframe,command=self.update_data,text="Update", bg="white", fg="blue", font=("arial", 12, "bold"),
                             width=32, height=2, padx=2, pady=6)
    btnUpdate.grid(row=0,column=2)

    btDelete = Button(Buttonframe, command=self.idelete,text="Delete", bg="white", fg="blue", font=("arial", 12, "bold"),
                       width=32, height=2, padx=2, pady=6)
    btDelete.grid(row=0, column=3)

    btClear = Button(Buttonframe,command=self.clear, text="Clear", bg="white", fg="blue", font=("arial", 12, "bold"),
                      width=32, height=2, padx=2, pady=6)
    btClear.grid(row=0, column=4)

    btnExit = Button(Buttonframe, command=self.Iexit,text="Exit", bg='white', fg="blue", font=("arial", 12, "bold",),
                      width=32, height=2, padx=2, pady=6)
    btnExit.grid(row=0, column=5)

    scroll_x=Scrollbar(orient=HORIZONTAL)
    scroll_Y=Scrollbar(Detailsframe,orient=VERTICAL)
    self.hospital_table=ttk.Treeview(Detailsframe,columns=("NameOftable","ref","dose","nooftablets","lot","issuedate",
            "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)
    scroll_x.pack(side = BOTTOM ,fill=X)
    scroll_Y.pack (side = BOTTOM, fill=Y)

    scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
    scroll_Y=ttk.Scrollbar(command=self.hospital_table.yview)

    self.hospital_table.heading("NameOftable", text="Name Of Tablets")
    self.hospital_table.heading("ref", text="Name Of Tablets")
    self.hospital_table.heading("dose", text="Dose")
    self.hospital_table.heading("nooftablets", text="No Of Tablets")
    self.hospital_table.heading("lot", text="Lot")
    self.hospital_table.heading("issuedate", text="Ussue Date")
    self.hospital_table.heading("dailydose", text="Daily Date")
    self.hospital_table.heading("expdate", text="Exp Date")
    self.hospital_table.heading("storage", text="Storage")
    self.hospital_table.heading("nhsnumber", text="NHS Number")
    self.hospital_table.heading("pname", text="Patient Name")
    self.hospital_table.heading("dob", text="DOB")
    self.hospital_table.heading("address", text="Address")

    self.hospital_table["show"]="headings"


    self.hospital_table.column("NameOftable",width=100)
    self.hospital_table.column("ref", width=100)
    self.hospital_table.column("dose", width=100)
    self.hospital_table.column("nooftablets", width=100)
    self.hospital_table.column("lot", width=100)
    self.hospital_table.column("issuedate", width=100)
    self.hospital_table.column("dailydose", width=100)
    self.hospital_table.column("expdate", width=100)
    self.hospital_table.column("storage", width=100)
    self.hospital_table.column("nhsnumber", width=100)
    self.hospital_table.column("pname", width=100)
    self.hospital_table.column("dob", width=100)
    self.hospital_table.column("address", width=100)

    self.hospital_table.pack(fill=BOTH, expand=1)
    self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
    self.fetch_data()





def iPrescriptionDate(self):
  if self.NameOftablet.get()=="" or self.ref()=="":
    messagebox.showerror("Error","All field are required")
  else:
    con=mysql.connector.connect(host="localhost",username="root",
                password="", port="",database="HospitalMS")
    my_cursor=con.cursor()
    my_cursor.execute("insert into hospital values=(%s,%s,%s,%s,%s,"
                      "%s,%s,%s,%s,%s,%s,%s,%s)",(
      self.NameOftablet.get(),
      self.ref.get(),
      self.Dose.get(),
      self.NumberofTablet.get(),
      self.Lot.get(),
      self.Issuedate.get(),
      self.ExpDate.get(),
      self.DailyDose.get(),
      self.StorageAdvice.get(),
      self.nhsNumber.get(),
      self.PatientName.get(),
      self.DateOfBirth.get(),
      self.PatientAddress.get()

    ) )

    con.commit()
    self.fetch_data()
    con.close()

def update_data(self):
  con = mysql.connector.connect(host="localhost", username="root",
                                password="", port="", database="HospitalMS")
  my_cursor = con.cursor()
  my_cursor.execute("update hospital set Name_of_tablets =%s,dose=%s,Numberoftablets=%s,"
                    "lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,"
                    "patientname=%s,DOB=%s,Patientaddress=%s,Referenc_No=%s",(self.NameOftablet.get(),
      self.ref.get(),
      self.Dose.get(),
      self.NumberofTablet.get(),
      self.Lot.get(),
      self.Issuedate.get(),
      self.ExpDate.get(),
      self.DailyDose.get(),
      self.StorageAdvice.get(),
      self.nhsNumber.get(),
      self.PatientName.get(),
      self.DateOfBirth.get(),
      self.PatientAddress.get()))

def fetch_data(self):
  con=mysql.connector.connect(host="localhost",username="root",
                password="", port="",database="HospitalMS")
  my_cursor=con.cursor()
  my_cursor.execute("select * from hospital")
  rows=my_cursor.fetchall()
  if len(rows)!=0:
    self.hospital_table.delete(*self.hospital_table.get_children())
    for i in rows:
      self.hospital_table.insert("",END,values=i)
    con.commit()
  con.close()

def get_cursor(self,event=""):
  cursor_row=self.hospital_table.focus()
  content=self.hospital_table.item(cursor_row)
  row=content["values"]
  self.NameOftablet.set(row[0])
  self.ref.set(row[1])
  self.Dose.set(row[2])
  self.NameOftablet.set(row[3])
  self.Issuedate.set(row[5])
  self.ExpDate.set(row[6])
  self.DailyDose.set(row[7])
  self.StorageAdvice.set(row[8])
  self.nhsNumber.set(row[9])
  self.PatientName.set(row[10])
  self.DateOfBirth.set(row[11])
  self.PatientAddress.set(row[12])


def iPrectioption(self):
  self.txtPrescription.insert(END, "name of Tablets:\t\t\t"+self.NameOftablet.get()+"\n")
  self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
  self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
  self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.NameOftablet.get() + "\n")
  self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
  self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
  self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.ExpDate.get() + "\n")
  self.txtPrescription.insert(END, "daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
  self.txtPrescription.insert(END, "side effect:\t\t\t" + self.sideEfect.get() + "\n")
  self.txtPrescription.insert(END, "Further information:\t\t\t" + self.FurtherInformation.get() + "\n")
  self.txtPrescription.insert(END, "StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n")
  self.txtPrescription.insert(END, "DrivingUsingMachine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
  self.txtPrescription.insert(END, "PatientId:\t\t\t" + self.PatientId.get() + "\n")
  self.txtPrescription.insert(END, "NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n")
  self.txtPrescription.insert(END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
  self.txtPrescription.insert(END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
  self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")

def idelete(self):
  con = mysql.connector.connect(host="localhost", username="root",
                                password="", port="", database="HospitalMS")
  my_cursor = con.cursor()
  query="delete from hospital where Referenc_No=%s"
  value=(self.ref.get(),)
  my_cursor.execute(query,value)

  con.commit()
  con.close()
  self.fetch_data()
  messagebox.showinfo("Delete","Patient has been deleted succesfully")


def clear(self):
  self.NameOftablet.set("")
  self.ref.set("")
  self.Dose.set("")
  self.NumberofTablet.set("")
  self.Lot.set("")
  self.Issuedate.set("")
  self.ExpDate.set("")
  self.DailyDose.set("")
  self.sideEfect.set("")
  self.FurtherInformation.set("")
  self.StorageAdvice.set("")
  self.DrivingUsingMachine.set("")
  self.HowtoUseMedication.set("")
  self.PatientId.set("")
  self.nhsNumber.set("")
  self.PatientName.set("")
  self.DateOfBirth.set("")
  self.PatientAddress.set("")
  self.txtPrescription.delete("1.0",END)

def Iexit(self):
  iExit=messagebox.askyesno("Hospital Management system","Confirm you want to exit")
  if iExit>0:
    root.destroy()
    return

root=Tk()
ob=Hospital(root)
root.mainloop()