import matlab.engine

mdl = "IPMSMAxleDriveEVDQ"   # your model
Ts = 0.002
ep_time = 0.02

eng = matlab.engine.start_matlab()
h = eng.init_ev_noedit(mdl, Ts, 0.0, ep_time, nargout=1)

out = eng.step_ev_noedit(h, 0.5, 0.0, 2.0, 5.0, nargout=1)

print("names:", list(out["names"]))
print("Treq:", float(out["Treq"]), "Te:", float(out["Te"]), "w:", float(out["w"]))
