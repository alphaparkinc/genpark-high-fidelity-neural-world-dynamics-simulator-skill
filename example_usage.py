from client import HighFidelityNeuralWorldDynamicsSimulatorClient

def main():
    client = HighFidelityNeuralWorldDynamicsSimulatorClient()
    res = client.simulate_world_physics('Cloth drapery fluttering in supersonic shockwave tunnel', 90)
    print('Neural World Simulator: ' + res['simulation_job_id'] + ' (Resolution: ' + res['rendered_resolution'] + ')')
    print('Physics Fidelity: ' + str(res['physics_fidelity_score_pct']) + '% | Optical Consistency: ' + str(res['optical_refraction_consistency_pct']) + '%')
    print('Solver: ' + res['fluid_viscosity_model'])
    print('Video Output: ' + res['simulation_mp4_url'])

if __name__ == '__main__':
    main()
