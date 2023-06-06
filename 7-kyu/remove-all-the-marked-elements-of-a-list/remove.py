class List:
    def remove_(self, integer_list, values_list):
        #your code here
        
        for v in values_list:
            flag = True
            
            while flag:
                if v in integer_list:

                    integer_list.remove(v)

                else:
                    
                    flag = False
                    
        
        return integer_list