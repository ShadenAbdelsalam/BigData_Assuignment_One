FROM ubuntu:latest

# Install python and dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

# Set working directory
WORKDIR /home/doc-bd-a1

# Copy dataset file
COPY bd-a1/StudentsPerformance.csv /home/doc-bd-a1

# Install necessary libraries
RUN pip3 install pandas numpy scikit-learn scipy matplotlib seaborn

# Open bash shell
# CMD ["bin/bash"]