import numpy as np

T= np.array([[1,1,1],
            [1,1,1],
            [1,1,1]])
F= 2*T; R= 3*T; L= 4*T; B=5*T; D= 6*T

# rot= input('Enter the rotation= ')

def rotation(rot):
    if (rot == 'u' or rot == 'U'):
        Ver_u = np.vstack((T, F, R, L, B, D))
        Ver_u[[3, 6, 9, 12]] = Ver_u[[6, 12, 3, 9]]
        F = Ver_u[3:6]
        R = Ver_u[6:9]
        L = Ver_u[9:12]
        B = Ver_u[12:15]
    elif (rot == 'u1' or rot == 'U1'):
        Ver_u1 = np.vstack((T, F, R, L, B, D))
        Ver_u1[[3, 6, 9, 12]] = Ver_u1[[9, 3, 12, 6]]
        F = Ver_u1[3:6]
        R = Ver_u1[6:9]
        L = Ver_u1[9:12]
        B = Ver_u1[12:15]
    elif (rot == 'd' or rot == 'D'):
        Ver_d = np.vstack((T, F, R, L, B, D))
        Ver_d[[5, 8, 11, 14]] = Ver_d[[11, 5, 14, 8]]
        F = Ver_d[3:6]
        R = Ver_d[6:9]
        L = Ver_d[9:12]
        B = Ver_d[12:15]
    elif (rot == 'd1' or rot == 'D1'):
        Ver_d1 = np.vstack((T, F, R, L, B, D))
        Ver_d1[[5, 8, 11, 14]] = Ver_d1[[8, 14, 5, 11]]
        F = Ver_d1[3:6]
        R = Ver_d1[6:9]
        L = Ver_d1[9:12]
        B = Ver_d1[12:15]
    elif (rot == 'r' or rot == 'R'):
        Hor_r = np.hstack((T, F, R, L, B, D))
        Hor_r[:, [2, 5, 14, 17]] = Hor_r[:, [5, 17, 2, 14]]
        T = Hor_r[:, [0, 1, 2]]
        F = Hor_r[:, [3, 4, 5]]
        B = Hor_r[:, [12, 13, 14]]
        D = Hor_r[:, [15, 16, 17]]
    elif (rot == 'r1' or rot == 'R1'):
        Hor_r1 = np.hstack((T, F, R, L, B, D))
        Hor_r1[:, [2, 5, 14, 17]] = Hor_r1[:, [14, 2, 17, 5]]
        T = Hor_r1[:, [0, 1, 2]]
        F = Hor_r1[:, [3, 4, 5]]
        B = Hor_r1[:, [12, 13, 14]]
        D = Hor_r1[:, [15, 16, 17]]
    elif (rot == 'l' or rot == 'L'):
        Hor_l = np.hstack((T, F, R, L, B, D))
        Hor_l[:, [0, 3, 12, 15]] = Hor_l[:, [12, 0, 15, 3]]
        T = Hor_l[:, [0, 1, 2]]
        F = Hor_l[:, [3, 4, 5]]
        B = Hor_l[:, [12, 13, 14]]
        D = Hor_l[:, [15, 16, 17]]
    elif (rot == 'l1' or rot == 'L1'):
        Hor_l1 = np.hstack((T, F, R, L, B, D))
        Hor_l1[:, [0, 3, 12, 15]] = Hor_l1[:, [3, 15, 0, 12]]
        T = Hor_l1[:, [0, 1, 2]]
        F = Hor_l1[:, [3, 4, 5]]
        B = Hor_l1[:, [12, 13, 14]]
        D = Hor_l1[:, [15, 16, 17]]
    elif (rot == 'f' or rot == 'F'):
        Hor_f = np.hstack((T, F, R, L, B, D))
        T_a = Hor_f[0:2, 0:3]
        L_c = Hor_f[:, 11]
        T = np.append(T_a, [L_c], axis=0)
        R_a = Hor_f[0:3, 7:9]
        T_c = Hor_f[2:3, 0:3]
        R = np.transpose(np.vstack([T_c, np.transpose(R_a)]))
        L_c = Hor_f[0:3, 9:11]
        D_a = Hor_f[0:1, 15:18]
        L = np.transpose(np.vstack([np.transpose(L_c), D_a]))
        D_bc = Hor_f[1:3, 15:18]
        R_a_col = Hor_f[:, 6]
        D = np.append(D_bc, [np.transpose(R_a_col)], axis=0)
        D[[0, 2]] = D[[2, 0]]
    elif (rot == 'f1' or rot == 'F1'):
        Hor_f1 = np.hstack((T, F, R, L, B, D))
        T_a = Hor_f1[0:2, 0:3]
        R_c = Hor_f1[:, 6]
        T = np.append(T_a, [R_c], axis=0)
        R_a = Hor_f1[0:3, 7:9]
        D_a = Hor_f1[0:1, 15:18]
        R = np.transpose(np.vstack([D_a, np.transpose(R_a)]))
        L_c = Hor_f1[0:3, 9:11]
        T_c = Hor_f1[2:3, 0:3]
        L = np.transpose(np.vstack([np.transpose(L_c), T_c]))
        D_bc = Hor_f1[1:3, 15:18]
        L_a_col = Hor_f1[:, 11]
        D = np.append(D_bc, [np.transpose(L_a_col)], axis=0)
        D[[0, 2]] = D[[2, 0]]
    elif (rot == 'm' or rot == 'M'):
        Hor_m = np.hstack((T, F, R, L, B, D))
        Hor_m[:, [1, 4, 13, 16]] = Hor_m[:, [4, 16, 1, 13]]
        T = Hor_m[:, [0, 1, 2]]
        F = Hor_m[:, [3, 4, 5]]
        B = Hor_m[:, [12, 13, 14]]
        D = Hor_m[:, [15, 16, 17]]

#
# if (rot == 'u' or rot == 'U'):
#     Ver_u = np.vstack((T, F, R, L, B, D))
#     Ver_u[[3, 6, 9, 12]]= Ver_u[[6, 12, 3, 9]]
#     F= Ver_u[3:6]; R= Ver_u[6:9]; L= Ver_u[9:12]; B= Ver_u[12:15]
# elif (rot == 'u1' or rot == 'U1'):
#     Ver_u1 = np.vstack((T, F, R, L, B, D))
#     Ver_u1[[3, 6, 9, 12]]= Ver_u1[[9, 3, 12, 6]]
#     F= Ver_u1[3:6]; R= Ver_u1[6:9]; L= Ver_u1[9:12]; B= Ver_u1[12:15]
# elif (rot == 'd' or rot == 'D'):
#     Ver_d = np.vstack((T, F, R, L, B, D))
#     Ver_d[[5, 8, 11, 14]]= Ver_d[[11, 5, 14, 8]]
#     F= Ver_d[3:6]; R= Ver_d[6:9]; L= Ver_d[9:12]; B= Ver_d[12:15]
# elif (rot == 'd1' or rot == 'D1'):
#     Ver_d1 = np.vstack((T, F, R, L, B, D))
#     Ver_d1[[5, 8, 11, 14]]= Ver_d1[[8, 14, 5, 11]]
#     F= Ver_d1[3:6]; R= Ver_d1[6:9]; L= Ver_d1[9:12]; B= Ver_d1[12:15]
# elif (rot == 'r' or rot == 'R'):
#     Hor_r = np.hstack((T, F, R, L, B, D))
#     Hor_r[:, [2, 5, 14, 17]]= Hor_r[:, [5, 17, 2, 14]]
#     T= Hor_r[:,[0,1,2]]; F= Hor_r[:,[3,4,5]]; B= Hor_r[:,[12,13,14]]; D= Hor_r[:,[15,16,17]]
# elif (rot == 'r1' or rot == 'R1'):
#     Hor_r1 = np.hstack((T, F, R, L, B, D))
#     Hor_r1[:, [2, 5, 14, 17]]= Hor_r1[:, [14, 2, 17, 5]]
#     T= Hor_r1[:,[0,1,2]]; F= Hor_r1[:,[3,4,5]]; B= Hor_r1[:,[12,13,14]]; D= Hor_r1[:,[15,16,17]]
# elif (rot == 'l' or rot == 'L'):
#     Hor_l = np.hstack((T, F, R, L, B, D))
#     Hor_l[:, [0, 3, 12, 15]]= Hor_l[:, [12, 0, 15, 3]]
#     T= Hor_l[:,[0,1,2]]; F= Hor_l[:,[3,4,5]]; B= Hor_l[:,[12,13,14]]; D= Hor_l[:,[15,16,17]]
# elif (rot == 'l1' or rot == 'L1'):
#     Hor_l1 = np.hstack((T, F, R, L, B, D))
#     Hor_l1[:, [0, 3, 12, 15]]= Hor_l1[:, [3, 15, 0, 12]]
#     T= Hor_l1[:,[0,1,2]]; F= Hor_l1[:,[3,4,5]]; B= Hor_l1[:,[12,13,14]]; D= Hor_l1[:,[15,16,17]]
# elif (rot == 'f' or rot == 'F'):
#     Hor_f = np.hstack((T, F, R, L, B, D))
#     T_a = Hor_f[0:2,0:3]; L_c = Hor_f[:, 11]
#     T= np.append(T_a,[L_c],axis= 0)
#     R_a = Hor_f[0:3, 7:9]; T_c = Hor_f[2:3, 0:3]
#     R= np.transpose(np.vstack([T_c,np.transpose(R_a)]))
#     L_c = Hor_f[0:3, 9:11]; D_a = Hor_f[0:1, 15:18]
#     L = np.transpose(np.vstack([np.transpose(L_c), D_a]))
#     D_bc = Hor_f[1:3, 15:18]; R_a_col = Hor_f[:, 6]
#     D= np.append(D_bc, [np.transpose(R_a_col)], axis=0)
#     D[[0, 2]] = D[[2, 0]]
# elif (rot == 'f1' or rot == 'F1'):
#     Hor_f1 = np.hstack((T, F, R, L, B, D))
#     T_a = Hor_f1[0:2,0:3]; R_c = Hor_f1[:, 6]
#     T= np.append(T_a,[R_c],axis= 0)
#     R_a = Hor_f1[0:3, 7:9]; D_a = Hor_f1[0:1, 15:18]
#     R= np.transpose(np.vstack([D_a,np.transpose(R_a)]))
#     L_c = Hor_f1[0:3, 9:11]; T_c = Hor_f1[2:3, 0:3]
#     L = np.transpose(np.vstack([np.transpose(L_c), T_c]))
#     D_bc = Hor_f1[1:3, 15:18]; L_a_col = Hor_f1[:, 11]
#     D= np.append(D_bc, [np.transpose(L_a_col)], axis=0)
#     D[[0, 2]] = D[[2, 0]]
# elif (rot == 'm' or rot == 'M'):
#     Hor_m = np.hstack((T, F, R, L, B, D))
#     Hor_m[:, [1, 4, 13, 16]]= Hor_m[:, [4, 16, 1, 13]]
#     T= Hor_m[:,[0,1,2]]; F= Hor_m[:,[3,4,5]]; B= Hor_m[:,[12,13,14]]; D= Hor_m[:,[15,16,17]]


# Bottom cross (White)
bottom_white = np.hstack((T, F, R, L, B, D))
count_white = []


if bottom_white[0,[16]]== 6:
    count_white.append(1)
else:
    count_white.append(0)
if bottom_white[1,[17]] == 6:
    count_white.append(1)
else:
    count_white.append(0)
if bottom_white[2,[16]]== 6:
    count_white.append(1)
else:
    count_white.append(0)
if bottom_white[1,[15]] == 6:
    count_white.append(1)
else:
    count_white.append(0)

no_white = np.sum(count_white)

# for cross in range(4):
if count_white[0] == 1:
    if bottom_white[1,[4]] == bottom_white[2,[4]]:
        pass
    else:
        rotation('f')
        rotation('f')
else:
    pass






































































