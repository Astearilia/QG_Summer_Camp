import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

leader_position = np.array((20.0, 50.0))
follower_position = np.zeros((3, 2))
follower_position[0, :] = np.array((6, 60))
follower_position[1, :] = np.array((10, 40))
follower_position[2, :] = np.array((16, 70))

leader_velocity = np.array((6.0, 0))
follower_velocity = np.zeros((3, 2))
follower_velocity[0, :] = np.array((10, 5))
follower_velocity[1, :] = np.array((8, 4))
follower_velocity[2, :] = np.array((9, 3))

velocity_L = leader_velocity[:]
alpha = np.zeros((3, 3))
flag_connect_0_other = 0

if flag_connect_0_other != 1:
    alpha[0, :] = np.array((0, 0, 0))
    alpha[1, :] = np.array((0, 0, 1))
    alpha[2, :] = np.array((0, 1, 0))
else:
    alpha[0, :] = np.array((0, 1, 1))
    alpha[1, :] = np.array((1, 0, 1))
    alpha[2, :] = np.array((1, 1, 0))

k = np.array((0, 10, 10))

beta = 1
gamma = 1

r_leader = np.array((-15, -10, -5))
r_ij = np.zeros((3, 3, 2))
r_ij[0, :, 0] = np.array((0, -5, -10))
r_ij[0, :, 1] = np.zeros((3, 1)).reshape(3)
r_ij[1, :, 0] = np.array((5, 0, -5))
r_ij[1, :, 1] = np.zeros((3, 1)).reshape(3)
r_ij[2, :, 0] = np.array((10, 5, 0))
r_ij[2, :, 1] = np.zeros((3, 1)).reshape(3)
r = np.zeros((3, 2))
r[0, :] = np.array((-15, 0))
r[1, :] = np.array((-10, 0))
r[2, :] = np.array((-5, 0))

T = 10
rounds = 100
delta_t = T / rounds
position_map = np.zeros((rounds, 4, 2))
velocity_map = np.zeros((rounds, 4, 2))

for t in range(rounds):
    leader_position[:] += leader_velocity[:] * delta_t
    for i in range(4):
        if i == 0:
            position_map[t,i,:]=leader_position[:]
            velocity_map[t,i,:]=leader_velocity[:]
        else:
            position_map[t,i,:]=follower_position[i-1,:]
            velocity_map[t,i,:]=follower_velocity[i-1,:]
    for i in range(3):
        sum_tmp = np.zeros((3, 2))
        for j in range(3):
            sum_tmp[i, :] += alpha[i, j] *( (
                        follower_position[i, :] - follower_position[j, :] - r_ij[i, j, :]) + beta * (
                                         follower_velocity[i, :] - follower_velocity[j, :]))
        sum_tmp[i, :] += k[i] * (follower_position[i, :] - leader_position[:] - r[i, :] + gamma * (
                    follower_velocity[i, :] - leader_velocity[:]))
        follower_velocity[i, :] -= sum_tmp[i, :] * delta_t
        follower_position[i, :] += follower_velocity[i, :] * delta_t

c_list = ["blue", "black", "red"]

def draw_4(_t):
    plt.cla()
    for i, c in zip(range(1,4), c_list):
        plt.plot(position_map[:_t,i,0], position_map[:_t,i,1], c=c)
        plt.annotate('', xy=(position_map[_t,i,:]+velocity_map[_t,i,:]), xytext=(position_map[_t,i,:]),
                     arrowprops=dict( facecolor=c))
    plt.plot( position_map[:_t,0,0], position_map[:_t,0,1], c="purple")
    plt.annotate('', xy=(position_map[_t, 0, :] + velocity_map[_t, 0, :]), xytext=(position_map[_t, 0, :]),
                 arrowprops=dict( facecolor='purple'))
    plt.xlabel("X Position(m)")
    plt.ylabel("Y Position(m)")
    plt.xticks(range(0,100+1,20),range(0,100+1,20))
    plt.legend(["Vehicle i", "Vehicle i+1", "Vehicle i+2", "Leader"])
    plt.title("fig.4"if flag_connect_0_other else "fig 7")
fig_4 = plt.figure()
plt.yticks(range(40,71,10),labels=range(40,71,10))
an = ani.FuncAnimation(fig_4, draw_4, rounds)
an.save("fig_4.gif"if flag_connect_0_other else "fig_7.gif")
plt.show()


fig_5a=plt.figure()
for i,c in zip(range(1,4),c_list):
    plt.plot(range(rounds),position_map[:,i,0]-position_map[:,0,0],c=c)
plt.plot(range(rounds),position_map[:,0,0]-position_map[:,0,0],c='purple')
plt.legend(["Vehicle i", "Vehicle i+1", "Vehicle i+2", "Leader"])
plt.xlabel("Time(s)")
plt.ylabel("Longitudinal Gap(m)")
plt.xticks(range(0,rounds+1,10),range(T+1))
plt.yticks(range(-20,5,5))
plt.title('fig 5a'if flag_connect_0_other else "fig 8a")
plt.savefig('fig_5a.png'if flag_connect_0_other else "fig_8a.png")
plt.show()

fig_5b=plt.figure()
for i,c in zip(range(1,4),c_list):
    plt.plot(range(rounds),position_map[:,i,1]-position_map[:,0,1],c=c)
plt.plot(range(rounds),position_map[:,0,1]-position_map[:,0,1],c='purple')
plt.legend(["Vehicle i", "Vehicle i+1", "Vehicle i+2", "Leader"])
plt.xlabel("Time(s)")
plt.ylabel("Lateral Gap(m)")
plt.xticks(range(0,rounds+1,10),range(T+1))
plt.yticks(range(-10,21,5))
plt.title('fig 5b'if flag_connect_0_other else "fig 8b")
plt.savefig('fig_5b.png'if flag_connect_0_other else "fig_8b.png")
plt.show()

fig_6a=plt.figure()
for i,c in zip(range(1,4),c_list):
    plt.plot(range(rounds),velocity_map[:,i,0],c=c)
plt.plot(range(rounds),velocity_map[:,0,0],c='purple')
plt.legend(["Vehicle i", "Vehicle i+1", "Vehicle i+2", "Leader"])
plt.xlabel("Time(s)")
plt.ylabel("X-Velocity(m/s)")
plt.xticks(range(0,rounds+1,10),range(T+1))
plt.yticks(range(2,11,2))
plt.title('fig 6a'if flag_connect_0_other else "fig 9a")
plt.savefig('fig_6a.png'if flag_connect_0_other else "fig_9a.png")
plt.show()

fig_6b=plt.figure()
for i,c in zip(range(1,4),c_list):
    plt.plot(range(rounds),velocity_map[:,i,1],c=c)
plt.plot(range(rounds),velocity_map[:,0,1],c='purple')
plt.legend(["Vehicle i", "Vehicle i+1", "Vehicle i+2", "Leader"])
plt.xlabel("Time(s)")
plt.ylabel("Y-Velocity(m/s)")
plt.xticks(range(0,rounds+1,10),range(T+1))
plt.yticks(range(-24,17,2))
plt.title('fig 6b'if flag_connect_0_other else "fig 9b")
plt.savefig('fig_6b.png'if flag_connect_0_other else "fig 9b")
plt.show()