from pyscript import display, document


def getting_info(e):
    sub1 = float(document.getElementById("sci").value)
    sub2 = float(document.getElementById("eng").value)
    sub3 = float(document.getElementById("ict").value)
    sub4 = float(document.getElementById("math").value)
    sub5 = float(document.getElementById("fili").value)
    sub6 = float(document.getElementById("pe").value)

    first_name = document.getElementById("fname").value
    last_name = document.getElementById("lname").value

    sci = 5
    eng = 5
    ict = 2
    math = 5
    fili = 3
    pe = 1

    total_average = sci + eng + ict + math + fili + pe
    calculate = ((sub1*sci)+(sub2*eng)+(sub3*ict)+(sub4*math)+(sub5*fili)+(sub6*pe)) / (total_average) 

    message = f"""
    Name: {first_name} {last_name}\n
    Science: {sub1}\n
    English: {sub2}\n
    ICT: {sub3}\n
    Math: {sub4}\n
    Filipino: {sub5}\n
    PE: {sub6}\n

    Your General Weighted Average is: {calculate:.2f}
    """

    display(message, target="output")


def club1_information(e):
    
    club1 ={
        'Club Name':'Club Name: Winx Club',
        'Description':'Description: learn how to use your  magical powers to protect the Magic Dimension from dark forces. Utilize your powers and bonds to defeat villains like the Trix, a trio of witches.',
        'Meeting Time':'Meeting Time: Mondays and Wednesdays at 3:00pm',
        'Location':'Location: Libarary',
        'Club Moderator':'Club Moderator: Bloom',
        'Number of members':'Number of Members: 6'
    }

    display(f'{club1['Club Name']} {club1['Description']} {club1['Meeting Time']} {club1['Location']} {club1['Club Moderator']} {club1['Number of members']}', target="output")

def club2_information(e):
    club2 ={
        'Club Name':'Club Name: Specialists',
        'Description':'Description: Non-magical warriors trained in the art of combat. ',
        'Meeting Time':'Meeting Time: Mondays and Wednesdays at 3:00pm.',
        'Location':'Location: Red Fountain',
        'Club Moderator':'Club Moderator: Riven',
        'Number of members':'Number of Members: 5'
    }

    display(f'{club2['Club Name']} {club2['Description']} {club2['Meeting Time']} {club2['Location']} {club2['Club Moderator']} {club2['Number of members']}', target="output")

def club3_information(e):
    club3 ={
        'Club Name':'Club Name: Trix',
        'Description':'Description:  As the descendants of the most powerful evil witches, their club is centered around malicious and power-hungry goals, such as conquering the Magical Dimension.  ',
        'Meeting Time':'Meeting Time: Tuesday and Thursday at 3:00pm',
        'Location':'Location: Cloud Tower',
        'Club Moderator':'Club Moderator: Icy',
        'Number of members':'Number of Members: 3'
    }


    display(f'{club3['Club Name']} {club3['Description']} {club3['Meeting Time']} {club3['Location']} {club3['Club Moderator']} {club3['Number of members']}', target="output")


