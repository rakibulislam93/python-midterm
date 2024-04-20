
class Star_Cinema:
    _hall_list = [] # protected...

    def entry_hall(self,hall):
        self._hall_list.append(hall)
    
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.__seats = {(row,col):'O'for row in range(rows)for col in range(cols)} # private..
        self.__show_list = []  # private..
        super().entry_hall(hall_no)


    def entry_show(self,id,movie_name,time):
        self.__show_list.append((id,movie_name,time))
    
    def book_seats(self,show_id,stor_seat):
        stor_id = [show[0]for show in self.__show_list]

        if show_id not in stor_id:
            print('Error : Invalid show id')
            return

        for row,col in stor_seat:
            if (row,col) not in self.__seats:
                print('Error : Invalid seats.')
                return
            
            if self.__seats[(row,col)]=='X':
                print(f'Error : Seats {row,col} is Already booking..')
                return
                         
            self.__seats[(row,col)]='X'
        
        print('Seats booking Successfully..')
        

    def view_show_list(self):
        print('\n\t...Current running shows...')
        for show in self.__show_list:
            print(f'Show ID : {show[0]} Movie : {show[1]} Time : {show[2]}')

    def view_available_seats(self,show_id):
        stor_id = [show[0]for show in self.__show_list]
        
        if show_id not in stor_id:
            print('Eroor : Invalid show id..')
            return

        print('\n\t...Available Seats...')
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.__seats[(row,col)], end=' ')
            print()


hall_1 = Hall(rows=5, cols=10, hall_no=1)
hall_2 = Hall(rows=4,cols=5,hall_no=2)

hall_2.entry_show(id='C1',movie_name='Rajkumar',time='8:00 PM')

hall_1.entry_show(id='S1', movie_name='Avengers', time='12:00 PM')
hall_1.entry_show(id='S2', movie_name='Spider-Man', time='3:00 PM')
hall_1.entry_show(id='S3', movie_name='Jawan', time='5:00 PM')

while True:

    print("1. View Shows")
    print("2. View Available Seats")
    print("3. Booking for Seats")
    print("4. Exit")

    choice = int(input('Enter your choice : '))

    if choice==1:
        hall_1.view_show_list()
    
    elif choice==2:
        show_id = input('Enter the Show ID for Available seats : ')
        hall_1.view_available_seats(show_id)
    
    elif choice==3:
        show_id = input('Enter the Show Id for booking seats : ')

        num_seat = int(input('How many seats you booked : '))
        stor_seat = []

        for _ in range(num_seat):
            row = int(input('Enter the row number : '))
            col = int(input('Enter the column number : '))
            stor_seat.append((row,col))
        
        hall_1.book_seats(show_id,stor_seat)
    
    elif choice==4:
        print('Exit the Programm..')
        break;
    else:
        print('Invalid choice. Please choice valid option..')
