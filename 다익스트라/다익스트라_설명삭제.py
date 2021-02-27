def search( maps, middlePoints, start, end ):

    distances = maps[ start ]
    through = middlePoints[ start ] 
    
    others = list( distances.keys() )
    isChecked = { i : False for i in others }
    isChecked[ start ] = True

    
    while( False in list( isChecked.values() ) ):
        
        shortest = { 'name' : '',
                    'distance' : '?' }

        for name, distance in distances.items() :
            if ( not isChecked[ name ] ) and ( not distance == '?' ) :    
                if shortest[ 'distance' ] == '?':
                    shortest[ 'name' ] = name
                    shortest[ 'distance'] = distance
                        
                elif shortest[ 'distance'] >  distance:
                    shortest[ 'name'] = name
                    shortest['distance'] = distance
                    
        checkingRoute = maps[ shortest[ 'name' ] ]
        
        for name, distance in checkingRoute.items():
            
            if not distance == '?':
                nowDistance = distances[ shortest[ 'name' ] ] + distance
                
                if distances[ name ] == '?':
                    distances[ name ] = nowDistance
                    through[ name ] = shortest[ 'name' ]
                    
                elif distances[ name ] > nowDistance:
                    distances[ name ] = nowDistance
                    through[ name ] = shortest[ 'name' ]
            
                   
        isChecked[ shortest['name'] ] = True

    return distances       
    




maps = {'A' : {'A' : 0,
                 'B' : 3,
                 'C' : 2,
                 'D' : 4,
                 'E' : '?',
                 'F' : '?'} ,
         
         'B' : { 'A' : 3,
                 'B' : 0,
                 'C' : '?',
                 'D' : 2,
                 'E' : '?',
                 'F' : 5},
         
         'C' : { 'A' : 2,
                 'B' : '?',
                 'C' : 0,
                 'D' : '?',
                 'E' : 1,
                 'F' : '?'},
         
         'D' : { 'A' : 4,
                 'B' : 2,
                 'C' : '?',
                 'D' : 0,
                 'E' : 1,
                 'F' : 3},
         
         'E' : { 'A' : '?',
                 'B' : '?',
                 'C' : 1,
                 'D' : 1,
                 'E' : 0,
                 'F' : 2},
         
         'F' : { 'A' : '?',
                 'B' : 5,
                 'C' : '?',
                 'D' : 3,
                 'E' : 2,
                 'F' : 0,},

         }

middlePoints = { 'A' : { 'A' : 'A',
                         'B' : 'A',
                         'C' : 'A',
                         'D' : 'A',
                         'E' : '?',
                         'F' : '?'} ,
         
                 'B' : { 'A' : 'B',
                         'B' : 'B',
                         'C' : '?',
                         'D' : 'B',
                         'E' : '?',
                         'F' : 'B'},
                 
                 'C' : { 'A' : 'C',
                         'B' : '?',
                         'C' : 'C',
                         'D' : '?',
                         'E' : 'C' ,
                         'F' : '?'},
                 
                 'D' : { 'A' : 'D' ,
                         'B' : 'D' ,
                         'C' : '?',
                         'D' : 'D',
                         'E' : 'D' ,
                         'F' : 'D' },
                 
                 'E' : { 'A' : '?',
                         'B' : '?',
                         'C' : 'E',
                         'D' : 'E',
                         'E' : 'E',
                         'F' : 'E'},
                 
                 'F' : { 'A' : '?',
                         'B' : 'F',
                         'C' : '?',
                         'D' : 'F',
                         'E' : 'F',
                         'F' : 'F'},

                 }


start = input("누구부터? : ")
end = input("누구까지? : ")

result = search( maps, middlePoints, start, end )

print( start, "에서부터의 최단거리는")

for name, distance in result.items():
    print( name , "까지",distance ,  )
    
print("이며,",end,"까지는",result[end],"입니다.")

