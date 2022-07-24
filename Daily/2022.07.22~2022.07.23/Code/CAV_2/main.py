import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

vehicle_num = 6
leader_num = 2
case = 1
platoon_num_vehicle = np.zeros((vehicle_num - leader_num)).astype(int)
platoon_num_vehicle_0 = np.zeros(leader_num).astype(int)
T = 10
rounds = 100
beta = 1
gamma_0 = 1
gamma_1 = 1
leader_position = np.zeros((leader_num, 2))
follower_position = np.zeros((vehicle_num - leader_num, 2))
leader_velocity = np.zeros((leader_num, 2))
follower_velocity = np.zeros((vehicle_num - leader_num, 2))
a = np.zeros((leader_num, vehicle_num - leader_num, vehicle_num - leader_num))
r_PL = np.zeros((leader_num, vehicle_num - leader_num, 2))
r_RL = np.zeros((leader_num, vehicle_num - leader_num, 2))
r_ij = np.zeros((leader_num, vehicle_num - leader_num, vehicle_num - leader_num))
r_Lq = np.zeros((leader_num, 2))
r_LL = np.zeros((leader_num, leader_num))
b = np.zeros((leader_num, 4))
c = np.zeros((leader_num, 4))

if case == 0:
    platoon_num_vehicle_0 = np.array((4, 0)).astype(int)
    platoon_num_vehicle[:] = np.array((1, 1, 1, 1)).astype(int)
    leader_position[0, :] = np.array((60, 1))
    leader_position[1, :] = np.array((10, 1))
    follower_position[0, :] = np.array((40, 1))
    follower_position[1, :] = np.array((40, 2))
    follower_position[2, :] = np.array((30, 1))
    follower_position[3, :] = np.array((30, 2))

    leader_velocity[0, :] = np.array((10, 0))
    leader_velocity[1, :] = np.array((10, 0))
    follower_velocity[0, :] = np.array((10, 0))
    follower_velocity[1, :] = np.array((10, 0))
    follower_velocity[2, :] = np.array((10, 0))
    follower_velocity[3, :] = np.array((10, 0))

    a[0, 0, :] = np.array((0, 1, 0, 0))
    a[0, 1, :] = np.array((1, 0, 1, 0))
    a[0, 2, :] = np.array((0, 1, 0, 1))
    a[0, 3, :] = np.array((0, 0, 1, 0))

    r_ij[0, 0, :] = np.array((0, 10, 20, 30))
    r_ij[0, 1, :] = np.array((-10, 0, 10, 20))
    r_ij[0, 2, :] = np.array((-20, -10, 0, 10))
    r_ij[0, 3, :] = np.array((-30, -20, -10, 0))
    r_PL[0, 0, :] = np.array((-10, 0))
    r_PL[0, 1, :] = np.array((-20, 0))
    r_PL[0, 2, :] = np.array((-30, 0))
    r_PL[0, 3, :] = np.array((-40, 0))
    r_RL[0, 0, :] = np.array((40, 0))
    r_RL[0, 1, :] = np.array((30, 0))
    r_RL[0, 2, :] = np.array((20, 0))
    r_RL[0, 3, :] = np.array((10, 0))

    r_Lq[0, :] = np.array((0, 0))
    r_Lq[1, :] = np.array((-10, 0))
    r_LL[0, :] = np.array((0, 50))
    r_LL[1, :] = np.array((-50, 0))

    b[0, :] = np.array((1, 1, 1, 1)) * 2
    c[0, :] = np.array((1, 1, 1, 1)) * 2

if case == 1:
    platoon_num_vehicle_0 = np.array((2, 4)).astype(int)
    platoon_num_vehicle[:] = np.array((1, 1, 2, 2)).astype(int)
    leader_position[0, :] = np.array((80, 1))
    leader_position[1, :] = np.array((30, 2))
    follower_position[0, :] = np.array((70, 1))
    follower_position[1, :] = np.array((60, 1))
    follower_position[2, :] = np.array((20, 2))
    follower_position[3, :] = np.array((10, 2))

    leader_velocity[0, :] = np.array((10, 0))
    leader_velocity[1, :] = np.array((10, 0))
    follower_velocity[0, :] = np.array((10, 0))
    follower_velocity[1, :] = np.array((10, 0))
    follower_velocity[2, :] = np.array((10, 0))
    follower_velocity[3, :] = np.array((10, 0))

    r_PL[0, 0, :] = np.array((-10, 0))
    r_PL[0, 1, :] = np.array((-20, 0))
    r_PL[1, 2, :] = np.array((-10, 0))
    r_PL[1, 3, :] = np.array((-20, 0))
    r_RL[0, 0, :] = np.array((20, 0))
    r_RL[0, 1, :] = np.array((10, 0))
    r_RL[1, 2, :] = np.array((0, 0))
    r_RL[1, 3, :] = np.array((0, 0))

    r_Lq[0, :] = np.array((0, 0))
    r_Lq[1, :] = np.array((-10, 0))
    r_LL[0, :] = np.array((0, 30))
    r_LL[1, :] = np.array((-30, 0))

    b[0, :] = np.array((1, 1, 0, 0))
    b[1, :] = np.array((0, 0, 1, 1))
    c[0, :] = np.array((0, 1, 0, 0))
    c[1, :] = np.array((0, 0, 0, 0))

if case == 2:
    leader_num = 4
    vehicle_num = 10
    platoon_num_vehicle = np.zeros((vehicle_num - leader_num)).astype(int)
    platoon_num_vehicle_0 = np.zeros(leader_num).astype(int)
    leader_position = np.zeros((leader_num, 2))
    follower_position = np.zeros((vehicle_num - leader_num, 2))
    leader_velocity = np.zeros((leader_num, 2))
    follower_velocity = np.zeros((vehicle_num - leader_num, 2))
    a = np.zeros((leader_num, vehicle_num - leader_num, vehicle_num - leader_num))
    r_PL = np.zeros((leader_num, vehicle_num - leader_num, 2))
    r_RL = np.zeros((leader_num, vehicle_num - leader_num, 2))
    r_ij = np.zeros((leader_num, vehicle_num - leader_num, vehicle_num - leader_num))
    r_Lq = np.zeros((leader_num, 2))
    r_LL = np.zeros((leader_num,2))
    b = np.zeros((leader_num, vehicle_num-leader_num))
    c = np.zeros((leader_num, vehicle_num-leader_num))
    platoon_num_vehicle_0 = np.array((2, 4, 6)).astype(int)
    platoon_num_vehicle[:] = np.array((1, 1, 2, 2, 3, 3)).astype(int)
    # leader_position[0, :] = np.array((104, 1))
    # leader_position[1, :] = np.array((72, 1))
    # leader_position[2, :] = np.array((33, 1))
    # leader_position[3, :] = np.array((0, 1))
    # follower_position[0, :] = np.array((92, 1))
    # follower_position[1, :] = np.array((80, 2))
    # follower_position[2, :] = np.array((55, 1))
    # follower_position[3, :] = np.array((45, 1))
    # follower_position[4, :] = np.array((21, 1))
    # follower_position[5, :] = np.array((10, 1))

    # leader_position[0, :] = np.array((104, 1))
    # leader_position[1, :] = np.array((64, 1))
    # leader_position[2, :] = np.array((29, 1))
    # leader_position[3, :] = np.array((0, 1))
    # follower_position[0, :] = np.array((89, 1))
    # follower_position[1, :] = np.array((78, 2))
    # follower_position[2, :] = np.array((52, 1))
    # follower_position[3, :] = np.array((44, 1))
    # follower_position[4, :] = np.array((18, 1))
    # follower_position[5, :] = np.array((8, 2))

    leader_position[0, :] = np.array((104, 1))
    leader_position[1, :] = np.array((75, 1))
    leader_position[2, :] = np.array((35, 1))
    leader_position[3, :] = np.array((0, 1))
    follower_position[0, :] = np.array((93, 2))
    follower_position[1, :] = np.array((82, 2))
    follower_position[2, :] = np.array((60, 2))
    follower_position[3, :] = np.array((40, 2))
    follower_position[4, :] = np.array((17, 1))
    follower_position[5, :] = np.array((7, 2))

    leader_velocity[0, :] = np.array((10, 0))
    leader_velocity[1, :] = np.array((10, 0))
    follower_velocity[0, :] = np.array((10, 0))
    follower_velocity[1, :] = np.array((10, 0))
    follower_velocity[2, :] = np.array((10, 0))
    follower_velocity[3, :] = np.array((10, 0))
    follower_velocity[4, :] = np.array((10, 0))
    follower_velocity[5, :] = np.array((10, 0))

    r_PL[0, 0, :] = np.array((-10, 0))
    r_PL[0, 1, :] = np.array((-20, 0))
    r_PL[1, 2, :] = np.array((-10, 0))
    r_PL[1, 3, :] = np.array((-20, 0))
    r_PL[2, 4, :] = np.array((-10, 0))
    r_PL[2, 5, :] = np.array((-20, 0))
    r_RL[0, 0, :] = np.array((20, 0))
    r_RL[0, 1, :] = np.array((10, 0))
    r_RL[1, 2, :] = np.array((20, 0))
    r_RL[1, 3, :] = np.array((10, 0))
    r_RL[2, 4, :] = np.array((20, 0))
    r_RL[2, 5, :] = np.array((10, 0))

    r_Lq[0, :] = np.array((0, 0))
    r_Lq[1, :] = np.array((-10, 0))
    r_Lq[2, :] = np.array((-10, 0))
    r_Lq[3, :] = np.array((-10, 0))
    r_LL[0, :] = np.array((-30,0))
    r_LL[1, :] = np.array((-30,0))
    r_LL[2, :] = np.array((-30,0))
    r_LL[3, :] = np.array((-30,0))

    b[0, :] = np.array((1, 1, 0, 0, 0, 0))
    b[1, :] = np.array((0, 0, 1, 1, 0, 0))
    b[2, :] = np.array((0, 0, 0, 0, 1, 1))
    c[0, :] = np.array((0, 1, 0, 0, 0, 0))
    c[1, :] = np.array((0, 0, 0, 1, 0, 0))
    c[2, :] = np.array((0, 0, 0, 0, 0, 1))
d_L = np.ones((4, 1)) * 5

delta_t = T / rounds
position_map = np.zeros((rounds, vehicle_num, 2))
velocity_map = np.zeros((rounds, vehicle_num, 2))

for t in range(rounds):
    sum_tmp = np.zeros((leader_num, 2))
    for i in range(leader_num -1, 0, -1):
        sum_tmp[i, 0] = -d_L[0] * (leader_position[i, 0] - leader_position[i - 1, 0] - r_LL[i, 0]) - d_L[1] * (
                leader_velocity[i, 0] - leader_velocity[i - 1, 0]) - d_L[2] * (
                                leader_position[i, 0] - follower_position[
                            platoon_num_vehicle_0[i-1] - 1, 0] - r_Lq[
                                    i, 0]) - d_L[3] * (
                                leader_velocity[i, 0] - follower_velocity[
                            platoon_num_vehicle_0[i-1] - 1, 0])
        sum_tmp[i, 1] = -d_L[0] * (leader_position[i, 1] - leader_position[i - 1, 1] - r_LL[i, 1]) - d_L[1] * (
                leader_velocity[i, 1] - leader_velocity[i - 1, 1])
    leader_velocity[:, :] += sum_tmp[:, :] * delta_t
    leader_position[:, :] += leader_velocity[:, :] * delta_t
    sum_tmp = np.zeros((vehicle_num - leader_num, 2))
    for i, k in zip(range(vehicle_num - leader_num), platoon_num_vehicle):
        for j in range(vehicle_num - leader_num):
            sum_tmp[i, 0] += -a[k - 1, i, j] * (
                    gamma_0 * (follower_position[i, 0] - follower_position[j, 0] - r_ij[k - 1, i, j]) + gamma_1 * (
                    follower_velocity[i, 0] - follower_velocity[j, 0]))
        sum_tmp[i, 0] += -b[k - 1, i] * (
                gamma_0 * (follower_position[i, 0] - leader_position[k - 1, 0] - r_PL[k - 1, i, 0]) + gamma_1 * (
                follower_velocity[i, 0] - leader_velocity[0, 0]))
        if k != leader_num:
            sum_tmp[i, 0] += -c[k - 1, i] * (
                    gamma_0 * (follower_position[i, 0] - leader_position[k, 0] - r_RL[k - 1, i, 0]) + gamma_1 * (
                    follower_velocity[i, 0] - leader_velocity[1, 0]))
        sum_tmp[i, 1] = -b[k - 1, i] * (
                gamma_0 * (follower_position[i, 1] - leader_position[k - 1, 1] - r_PL[k - 1, i, 1]) + gamma_1 * (
                follower_velocity[i, 1] - leader_velocity[0, 1]))
    follower_velocity += sum_tmp[:, :] * delta_t
    follower_position += follower_velocity * delta_t
    for i in range(vehicle_num):
        if i < leader_num:
            position_map[t, i, :] = leader_position[i, :]
            velocity_map[t, i, :] = leader_velocity[i, :]
        else:
            position_map[t, i, :] = follower_position[i - leader_num, :]
            velocity_map[t, i, :] = follower_velocity[i - leader_num, :]

print(position_map[-1])

c_list = ["blue", "pink", "red", 'purple', 'green', 'yellow']
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False

# def draw_4(_t):
#     plt.cla()
#     for i, c in zip(range(0, vehicle_num), c_list):
#         plt.plot(position_map[:_t, i, 0], position_map[:_t, i, 1], c=c)
#         plt.annotate('', xy=(position_map[_t, i, :]), xytext=(position_map[_t, i, :] - velocity_map[_t, i, :]),
#                      arrowprops=dict(connectionstyle="arc3", facecolor=c))
#     plt.xlabel("X Position(m)")
#     plt.ylabel("Y Position(m)")
#     plt.xticks(range(0, 200 + 1, 20), range(0, 200 + 1, 20))
#     plt.legend(["L1", "L2", "F1", "F2", "F3", "F4"])
#     plt.title("fig 3"if case==0 else "fig 6")
# fig_4 = plt.figure()
# plt.yticks(range(40, 71, 10), labels=range(40, 71, 10))
# an = ani.FuncAnimation(fig_4, draw_4, rounds)
# an.save("fig_3.gif" if case==0 else "fig_6.gif")
# plt.show()
#
# fig_3 = plt.figure()
# for i, c in zip(range(0,vehicle_num), c_list):
#     plt.plot(position_map[:,i,0], position_map[:,i,1], c=c)
# plt.xlabel("X 位置(m)")
# plt.ylabel("Y 位置(m)")
# plt.xticks(range(0,200+1,20),range(0,200+1,20))
# plt.legend(["L1","L2","F1","F2","F3","F4"])
# plt.title("fig.3" if case==0 else "fig 6")
# plt.savefig('fig_3.png' if case==0 else "fig_6.png")
# plt.show()
#
#
# for i, c in zip(range(0,vehicle_num), c_list):
#     plt.plot(range(rounds),position_map[:,i,0],c=c)
# plt.xlabel("时间(s)")
# plt.ylabel("X位置(m)")
# plt.xticks(range(0,rounds+1,10),range(T+1))
# plt.yticks(range(10,161,10),labels=range(10,161,10))
# plt.legend(["L1","L2","F1","F2","F3","F4"])
# plt.title("fig 4a" if case==0 else "fig 7a")
# plt.savefig('fig_4a.png'if case==0 else "fig_7a.png")
# plt.show()
#
# for i, c in zip(range(0,vehicle_num), c_list):
#     plt.plot(range(rounds),position_map[:,i,1],c=c)
# plt.xlabel("时间(s)")
# plt.ylabel("Y位置(m)")
# plt.xticks(range(0,rounds+1,10),range(T+1))
# #plt.yticks(range(10,161,10),labels=range(10,161,10))
# plt.legend(["L1","L2","F1","F2","F3","F4"])
# plt.title("fig 4b" if case==0 else "fig 7b")
# plt.savefig('fig_4b.png' if case==0 else "fig_7b.png")
# plt.show()
#
# if case==0:
#     for j in range(leader_num):
#         for i, c in zip(range(leader_num,vehicle_num), c_list):
#             plt.plot(range(rounds),position_map[:,i,0]-position_map[:,j,0],c=c)
#     plt.xlabel("时间(s)")
#     plt.ylabel("纵向距离(m)")
#     plt.xticks(range(0,rounds+1,10),range(T+1))
#     plt.legend(["F1-L1","F2-L1","F3-L1","F4-L1","F1-L2","F1-L2","F2-L2","F3-L2","F4-L2"])
#     plt.title("fig 4c" )
#     plt.savefig('fig_4c.png' )
#     plt.show()
# if case==1:
#     for i,j, c in zip(range(leader_num,vehicle_num), platoon_num_vehicle,c_list):
#         plt.plot(range(rounds),position_map[:,i,0]-position_map[:,j-1,0],c=c)
#     plt.xlabel("时间(s)")
#     plt.ylabel("纵向距离(m)")
#     plt.xticks(range(0,rounds+1,10),range(T+1))
#     plt.legend(["F1-L1","F2-L1","F3-L2","F4-L2"])
#     plt.title("fig 7c" )
#     plt.savefig('fig_7c.png' )
#     plt.show()
#
# if case==0:
#     for j in range(leader_num):
#         for i, c in zip(range(leader_num,vehicle_num), c_list):
#             plt.plot(range(rounds),position_map[:,i,1]-position_map[:,j,1],c=c)
#     plt.xlabel("时间(s)")
#     plt.ylabel("横向距离(m)")
#     plt.xticks(range(0,rounds+1,10),range(T+1))
#     plt.legend(["F1-L1","F2-L1","F3-L1","F4-L1","F1-L2","F1-L2","F2-L2","F3-L2","F4-L2"])
#     plt.title("fig 4d")
#     plt.savefig('fig_4d.png')
#     plt.show()
# if case==1:
#     for i,j, c in zip(range(leader_num,vehicle_num), platoon_num_vehicle,c_list):
#         plt.plot(range(rounds),position_map[:,i,1]-position_map[:,j-1,1],c=c)
#     plt.xlabel("时间(s)")
#     plt.ylabel("横向距离(m)")
#     plt.xticks(range(0, rounds + 1, 10), range(T + 1))
#     plt.legend(["F1-L1","F2-L1","F3-L2","F4-L2"])
#     plt.title("fig 7d")
#     plt.savefig('fig_7d.png')
#     plt.show()
#
# for i, c in zip(range(0,vehicle_num), c_list):
#     plt.plot(range(rounds),velocity_map[:,i,0],c=c)
# plt.xlabel("时间(s)")
# plt.ylabel("X速度(m/s)")
# plt.xticks(range(0,rounds+1,10),range(T+1))
# plt.legend(["L1","L2","F1","F2","F3","F4"])
# plt.title("fig 4e"if case==0 else "fig 7e")
# plt.savefig('fig_4e.jpg'if case==0 else "fig_7e.png")
# plt.show()
#
# for i, c in zip(range(0,vehicle_num), c_list):
#     plt.plot(range(rounds),velocity_map[:,i,1],c=c)
# plt.xlabel("时间(s)")
# plt.ylabel("Y速度(m/s)")
# plt.xticks(range(0,rounds+1,10),range(T+1))
# plt.legend(["L1","L2","F1","F2","F3","F4"])
# plt.title("fig 4f"if case==0 else "fig 7f")
# plt.savefig('fig_4f.png'if case==0 else "fig_7f.png")
# plt.show()

# for i in zip(range(0,vehicle_num)):
#     plt.plot(range(rounds),position_map[:,i,0])
# plt.xlabel("时间(s)")
# plt.ylabel("X位置(m)")
# plt.xticks(range(0,rounds+1,10),range(T+1))
# plt.yticks(range(10,221,20),labels=range(10,221,20))
# plt.legend(["L1","L2","L3","L4","F1","F2","F3","F4","F5,", "F6" ])
# plt.title("fig 8f" )
# plt.savefig('fig_8f.png')
# plt.show()