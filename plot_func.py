import matplotlib.pyplot as plt
import math


def plot_cfg1(mongo_data):
    plt.subplots(1,2, figsize=(15,4))

    plt.subplot(1, 2, 1)
    plt.plot(mongo_data['date'], mongo_data['spo2'])
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('SpO2', fontsize=12)

    plt.axhline(94, color="green", linestyle=":", label="Negligible")
    plt.axhline(91, color="yellow", linestyle="--", label="Minor")
    plt.axhline(85, color="orange", linestyle="-.", label="Serious")
    plt.axhline(75, color="red", linestyle="-", label="Critical")

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

    plt.subplot(1, 2, 2)
    plt.plot(mongo_data['date'], mongo_data['heartRate'])
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Heart Rate', fontsize=12)

    plt.axhline(50, color="green", linestyle=":", label="Negligible")
    plt.axhline(45, color="yellow", linestyle="--", label="Minor")
    plt.axhline(40, color="orange", linestyle="-.", label="Serious")
    plt.axhline(35, color="red", linestyle="-", label="Critical")

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

    plt.show()

    
def plot_details_cfg1(mongo_data):
    fig, host = plt.subplots(figsize=(12,6))
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    par2.spines["right"].set_position(("axes", 1.15))
    par2.spines["right"].set_visible(True)

    x = mongo_data['date']
    p1, = host.plot(x, mongo_data['riskValue'], "r-", label="RiskValue")
    p2, = par1.plot(x, mongo_data['spo2'], "b-", label="SpO2")
    p3, = par2.plot(x,mongo_data['heartRate'], "g-", label="Heart Rate")

    host.set_xlabel("Date")
    host.set_ylabel("RiskValue", color='red')
    par1.set_ylabel("SpO2", color='blue')
    par2.set_ylabel("Heart Rate", color='green')

    host.set_ylim(math.floor(mongo_data['riskValue'].min() - 1), math.ceil(mongo_data['riskValue'].max()) + 1)
    par1.set_ylim(math.floor(mongo_data['spo2'].min() - 1), math.ceil(mongo_data['spo2'].max()) + 1) 
    par2.set_ylim(math.floor(mongo_data['heartRate'].min() - 1 ), math.ceil(mongo_data['heartRate'].max()) + 1)

    tkw = dict(size=4, width=1.6)
    host.tick_params(axis='y', **tkw)
    par1.tick_params(axis='y', **tkw)
    par2.tick_params(axis='y', **tkw)
    host.tick_params(axis='x', **tkw)

    critical = host.axhline(65, color="black", linestyle="-", label="Critical")
    serious = host.axhline(45, color="black", linestyle="-.", label="Serious")
    minor = host.axhline(25, color="black", linestyle="--", label="Minor")
    negligible = host.axhline(0, color="black", linestyle=":", label="Negligible")

    lines = [p1, p2, p3]
    risks = [critical, serious, minor, negligible]

    host.legend(lines, [l.get_label() for l in lines+ risks],
                loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

    legend1 = plt.legend(risks, [l.get_label() for l in risks], loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
    plt.gca().add_artist(legend1)

    plt.show()
    

def plot_cfg2(mongo_data):
    plt.subplots(1,2, figsize=(15,4))

    plt.subplot(1, 2, 1)
    plt.plot(mongo_data['date'], mongo_data['respirationRate'])
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Respiration Rate', fontsize=12)

    plt.axhline(11, color="green", linestyle=":", label="Negligible")
    plt.axhline(10, color="yellow", linestyle="--", label="Minor")
    plt.axhline(8, color="orange", linestyle="-.", label="Serious")
    plt.axhline(6, color="red", linestyle="-", label="Critical")

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

    plt.subplot(1, 2, 2)
    plt.plot(mongo_data['date'], mongo_data['etCO2'])
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('EtCO2', fontsize=12)

    plt.axhline(35, color="green", linestyle=":", label="Negligible")
    plt.axhline(31, color="yellow", linestyle="--", label="Minor")
    plt.axhline(25, color="orange", linestyle="-.", label="Serious")
    plt.axhline(20, color="red", linestyle="-", label="Critical")

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

    plt.show()

    
def plot_details_cfg2(mongo_data):
    fig, host = plt.subplots(figsize=(12,6))
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    par2.spines["right"].set_position(("axes", 1.15))
    par2.spines["right"].set_visible(True)

    x = mongo_data['date']
    p1, = host.plot(x, mongo_data['riskValue'], color="red", label="RiskValue")
    p2, = par1.plot(x, mongo_data['etCO2'], color="blue", label="EtCO2")
    p3, = par2.plot(x,mongo_data['respirationRate'], color="green", label="Respiration Rate")

    host.set_ylim(math.floor(mongo_data['riskValue'].min() - 1), math.ceil(mongo_data['riskValue'].max()) + 1)
    par1.set_ylim(math.floor(mongo_data['etCO2'].min() - 1), math.ceil(mongo_data['etCO2'].max()) + 1) 
    par2.set_ylim(math.floor(mongo_data['respirationRate'].min() - 1 ), math.ceil(mongo_data['respirationRate'].max()) + 1)

    host.set_xlabel("Date")
    host.set_ylabel("RiskValue", color='red')
    par1.set_ylabel("EtCO2", color='green')
    par2.set_ylabel("Respiration Rate", color='blue')

    tkw = dict(size=4, width=1.6)
    host.tick_params(axis='y', **tkw)
    par1.tick_params(axis='y', **tkw)
    par2.tick_params(axis='y', **tkw)
    host.tick_params(axis='x', **tkw)

    critical = host.axhline(65, color="black", linestyle="-", label="Critical")
    serious = host.axhline(45, color="black", linestyle="-.", label="Serious")
    minor = host.axhline(25, color="black", linestyle="--", label="Minor")
    negligible = host.axhline(0, color="black", linestyle=":", label="Negligible")


    lines = [p1, p2, p3]
    risks = [critical, serious, minor, negligible]

    host.legend(lines, [l.get_label() for l in lines+ risks],
                loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

    legend1 = plt.legend(risks, [l.get_label() for l in risks], loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
    plt.gca().add_artist(legend1)

    plt.show()