# Simple-Protection-using-privileges-and-sensitivity-levels



This medical data processing system is expected to have functionalities for reading and
writing data into a configuration file and into a data file using an appropriate method. User
data such as username, password, user type (patient or hospital staff), and privilege level are
stored in the configuration file. Passwords are protected by hashing using MD5. Privilege
levels are assigned for users considering their ability to access data in the data file.
The data file consists of data records for each user due to an encounter with a patient. Each
user has data records of four types personal detail, sickness details, drug prescriptions, and
lab test prescriptions. A certain user can have more than one record for a certain record type.
Each record is associated with sensitivity.
The ability to access data in the data file by users in the configuration file is determined by
the respective privileges and sensitivities.
### Assumptions
- There is a superuser (admin) account that has all the privileges to control
functionalities if required.
- Patients can register into the system directly.
- Hospital staff needs a code to register to ensure their privilege.
- There are different sensitivities for each record in the data file. These sensitivities can
be either assigned manually or otherwise, they are assigned default sensitivities
automatically.
- There are separate read and write sensitivity for each record.
- Data creating and deleting sensitivities are default added.

