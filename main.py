from frequency import letter_frequency as lf, utils, index_of_coincidence as ioc

def main():
    string = "May there be no reality that is beyond the one which we find ourselves in now"
    print(utils.total_letters("this is some text"))
    frequencies = utils.count_letters("this is some text")
    for key in frequencies:
        value = frequencies[key]
        if value != 0: 
            print(key,":",value)
    print(ioc.ioc("this Is SOMe text"))
    
if __name__ == "__main__":
    main()