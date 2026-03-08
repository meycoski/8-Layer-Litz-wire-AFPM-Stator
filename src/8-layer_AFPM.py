import pcbnew
import math

board = pcbnew.GetBoard()
layer_odds = [board.GetLayerID('F.Cu'), board.GetLayerID('In2.Cu'), 
              board.GetLayerID('In4.Cu'), board.GetLayerID('In6.Cu')]
layer_evens = [board.GetLayerID('In1.Cu'), board.GetLayerID('In3.Cu'), 
               board.GetLayerID('In5.Cu'), board.GetLayerID('B.Cu')]

center_x = 100.0
center_y = 100.0
num_poles = 12
N_strand = 5
track_width = 300000
via_size = 550000
via_drill = 250000

def get_xy(r, angle_deg):
    a = math.radians(angle_deg)
    return pcbnew.VECTOR2I(int((center_x + r * math.cos(a)) * 1000000), 
                           int((center_y + r * math.sin(a)) * 1000000))

def add_track(p1, p2, layer_id, width=track_width):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(p1)
    track.SetEnd(p2)
    track.SetWidth(width)
    track.SetLayer(layer_id)
    board.Add(track)
def add_via(pos_tuple, v_size=via_size, v_drill=via_drill):
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(pcbnew.VECTOR2I(int(pos_tuple[0]), int(pos_tuple[1])))
    via.SetWidth(v_size)
    via.SetDrill(v_drill)
    board.Add(via)

vias = set()
pad_r = 52.0
neutral_r = 14.0

for a in range(360):
    p1 = get_xy(neutral_r, a)
    p2 = get_xy(neutral_r, a+1)
    add_track(p1, p2, board.GetLayerID('B.Cu'), 1000000)

for phase in range(3):
    pad_angle = phase * 10.0 - 6.0 
    p_pad = get_xy(pad_r, pad_angle)
    add_via((p_pad.x, p_pad.y), 2500000, 1000000)
    
    for i in range(num_poles):
        for s in range(N_strand):
            
            r_out = 45.0 - s * 0.4
            r_in = 20.0 + s * 0.4
            angle_offset = phase * 10.0 + (s - 2) * 1.2
            
            a_out_start = i * 30.0 + angle_offset
            a_in_mid = i * 30.0 + 15.0 + angle_offset
            a_out_end = (i + 1) * 30.0 + angle_offset
            
            p_out_start = get_xy(r_out, a_out_start)
            p_in_mid = get_xy(r_in, a_in_mid)
            p_out_end = get_xy(r_out, a_out_end)
            
            vias.add((p_out_start.x, p_out_start.y))
            vias.add((p_in_mid.x, p_in_mid.y))
            
            if i < num_poles - 1: 
                vias.add((p_out_end.x, p_out_end.y))
            if i == 0:
                add_track(p_pad, p_out_start, board.GetLayerID('F.Cu'), track_width)
            if i == num_poles - 1:
                p_neutral = get_xy(neutral_r, a_in_mid)
                add_track(p_in_mid, p_neutral, board.GetLayerID('B.Cu'), track_width)
            for layer_id in layer_odds:
                add_track(p_out_start, p_in_mid, layer_id)
            if i < num_poles - 1:
                for layer_id in layer_evens:
                    add_track(p_in_mid, p_out_end, layer_id)

for v in vias:
    add_via(v)

pcbnew.Refresh()
print("Gercek U, V, W Padleri ve Notr Halkasi Olusturuldu!")
