def search( maps, middlePoints, start, end ):

    distances = maps[ start ]             # 받아온 maps 중, start 에서부터의 거리만 필요하므로, 일부만 분리시킵니다.
    through = middlePoints[ start ]       # middlePoints 도 마찬가지
    
    others = list( distances.keys() )              # others : 경유할 사람들 list 
    isChecked = { i : False for i in others }      # 각 사람들을 경유하는 루트를 확인해 보았는지 체크할 dict 입니다.  
    isChecked[ start ] = True                      # 아무도 경유하지 않는 ( 자기자신에서 바로 가는 경로) 는 이미 기록되었으므로 True 로 바꿔줍니다.

    
    while( False in list( isChecked.values() ) ):                       # isChecked 에 False 가 없으면 ( 즉, 모든 경유하는 경로를 체크해보았다면 ) 끝냅니다.
        
        shortest = { 'name' : '',                                       # shortest 에는 현재 체크해보지 않는 사람들 (경유 가능한 ) 중 가장 인접한 사람을 넣을겁니다.
                    'distance' : '?' }

        for name, distance in distances.items() :                      
            if ( not isChecked[ name ] ) and ( not distance == '?' ) :  # 이미 체크했다면 거릅니다. 거리가 '?'면 경유할 수 없습니다.   
                if shortest[ 'distance' ] == '?':                       # shortest[ 'distance' ] 가 '?' 면 distance가 무조건 작으므로 , 바로 shortest에 등록합니다.
                    shortest[ 'name' ] = name
                    shortest[ 'distance'] = distance
                        
                elif shortest[ 'distance'] >  distance:                 # ? 가 아닌 경우는 직접 비교하여 작을 때만 shortest를 바꿔줍니다.
                    shortest[ 'name'] = name
                    shortest['distance'] = distance
                    
        print( '\n', shortest[ 'name' ] , "을 경유하는 경로를 탐색합니다." )               # 경유할 사람 ( shortest[ 'name' ] ) 이 정해짐
        
        checkingRoute = maps[ shortest[ 'name' ] ]                                         # 경유할 사람에서 각 사람들까지의 거리
        
        for name, distance in checkingRoute.items():
            
            if not distance == '?':                                                # 거리가 '?' 면 인접한 ( 바로 갈 수 있는 ) 사람이 아님. 
                nowDistance = distances[ shortest[ 'name' ] ] + distance           # 경유할 사람에서 바로 갈 수 있는 사람이라면, 
                                                                                   #그 사람까지의 거리 = 경유할 사람까지의 거리 + 경유할 사람에서 바로 갈 수 있는 사람까지의 거리
                if distances[ name ] == '?':
                    distances[ name ] = nowDistance
                    through[ name ] = shortest[ 'name' ]
                    print("\n-", name, "까지 가는 ( 거리 :", nowDistance, ")인 경로를 발견하였습니다.")       # 현재 기록된 distance 와 nowDistance 를 비교하여 더 작은 값을 유지합니다.
                    
                elif distances[ name ] > nowDistance:
                    distances[ name ] = nowDistance
                    through[ name ] = shortest[ 'name' ]
                    print("\n-", name, "까지 가는 ( 거리 :", nowDistance, ")인 경로를 발견하였습니다.")
                    
                else:
                    print( "\n-", name, "까지 가는 ( 거리 :", nowDistance, ")인 경로를 발견하였으나 기존보다 멉니다.")
                    
        isChecked[ shortest['name'] ] = True                   # 반복문이 끝나면, 해당 사람을 경유하는 모든 경로를 체크하였으므로 isChecked[ shortest['name'] ] = True

        print( "\n결과 :", distances, '\n')

    return distances, through                                 # 최종결과 ( 거리, 경유 정보 ) 함께 리턴  
    








maps = {'A' : {'A' : 0,                         # maps 는 바로 인접해서 알 수 있는 상대까지의 거리만 기록해둡니다.
                 'B' : 3,                       # 나머지는 알 수 없으므로 '?' 로 기록합니다.
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

middlePoints = { 'A' : { 'A' : 'A',             # middlePoints 는 그 상대까지 가는데 경유해야할 마지막 사람을 기록합니다. 
                         'B' : 'A',             # 아무도 거치지 않고 바로 갈 수 있다면 자기 자신을 기록합니다.
                         'C' : 'A',             # 아직 알 수 없는 경우 '?' 로 기록합니다.
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


start = input("누구부터? : ")   # start : 자기자신 (입력)
end = input("누구까지? : ")     # end : 상대 (입력)

result, routes  = search( maps, middlePoints, start, end )  # 작성한 것들을 함수로 보낸 뒤, 최종 결과와 경로를 받아옵니다.

print( start, "에서부터의 최단거리는 \n")

for name, distance in result.items():

    route = name                      # ex) A에서 F 까지 가는 경로는 A -> .... -> routes[ routes[ F ] ] -> routes[ F ] -> F
    next = routes[ name ]
    while next != start:
        route = next + " -> " + route
        next = routes[ next ]
    route = start + " -> " + route
    
    print( name , "까지",distance , "(", route , ")" )
    
print("\n이며,",end,"까지는",result[end],"입니다.")


# https://www.youtube.com/watch?v=HFapeLxvdNg&t=346s
