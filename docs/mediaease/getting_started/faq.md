# MediaEase FAQ

Welcome to the **MediaEase FAQ**. Below, you'll find answers to common questions you may encounter during the installation and configuration process. If you experience an issue not covered here, feel free to refer to the documentation or seek assistance from the community.

---

<details>
  <summary><strong>Why is the installation stuck at "Configuring Sendmail"?</strong></summary>

  **Answer:**
  It's common for the installation to appear to hang during the "Configuring Sendmail" step. This is part of the process, and the setup of Sendmail can take a few minutes, especially during the initial configuration phase.
  
  - **Why does this happen?**  
    Sendmail is a complex service, and its configuration requires some time to complete. This is expected behavior, and you don’t need to worry unless the process takes an unusually long time.
  
  - **What should I do?**  
    Be patient and allow the configuration process to finish. No user interaction is required during this step, so simply wait for the process to complete. If it takes an unusually long time, ensure that your system resources and network connection are stable.

</details>

---

<details>
  <summary><strong>Why is the installation stuck at "Configuring HarmonyUI"?</strong></summary>

  **Answer:**
  The installation of HarmonyUI may appear to stall during its configuration due to the number of Composer (PHP) and Node.js dependencies it requires.

  - **Why does this happen?**  
    HarmonyUI relies on numerous dependencies to operate. Both PHP libraries via Composer and Node.js packages are installed during this step, which can take time depending on your network speed and system performance.
  
  - **What to expect:**  
    It's perfectly normal for this process to take a few minutes or more, depending on the speed of your system and internet connection. No interaction is necessary; just allow the dependencies to install. If the process takes significantly longer, you may want to verify your system's resource availability and network stability.

</details>

---

<details>
  <summary><strong>How long does it take to install MediaEase from a fresh server?</strong></summary>

  **Answer:**
  Installing MediaEase on a fresh server typically takes around **11 minutes** (test machine: 1vCPU). This duration may vary slightly depending on your server's specifications, network speed, and any additional tasks required during the setup process. If the installation takes significantly longer, it's advisable to check your server's performance and network connectivity to ensure everything is functioning as expected.

</details>
